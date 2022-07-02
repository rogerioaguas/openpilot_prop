#include <sys/resource.h>

#include <QApplication>
#include <QSslConfiguration>

#include "selfdrive/hardware/hw.h"
#include "selfdrive/ui/qt/qt_window.h"
#include "selfdrive/ui/qt/util.h"
#include "selfdrive/ui/qt/window.h"
#include "selfdrive/ui/qt/offroad/networking.h"


int main(int argc, char *argv[]) {
  setpriority(PRIO_PROCESS, 0, -20);

  qInstallMessageHandler(swagLogMessageHandler);
  initApp();

  if (Hardware::EON()) {
    QSslConfiguration ssl = QSslConfiguration::defaultConfiguration();
    ssl.setCaCertificates(QSslCertificate::fromPath("/usr/etc/tls/cert.pem"));
    QSslConfiguration::setDefaultConfiguration(ssl);
  }

  QApplication a(argc, argv);
  MainWindow w;
  setMainWindow(&w);
  addTetheringConnection();
  a.installEventFilter(&w);
  return a.exec();
}


void addTetheringConnection() {
  Connection connection;
  connection["connection"]["id"] = "Hotspot";
  connection["connection"]["uuid"] = QUuid::createUuid().toString().remove('{').remove('}');
  connection["connection"]["type"] = "802-11-wireless";
  connection["connection"]["interface-name"] = "wlan0";
  connection["connection"]["autoconnect"] = false;

  connection["802-11-wireless"]["band"] = "bg";
  connection["802-11-wireless"]["mode"] = "ap";
  connection["802-11-wireless"]["ssid"] = tethering_ssid.toUtf8();

  connection["802-11-wireless-security"]["group"] = QStringList("ccmp");
  connection["802-11-wireless-security"]["key-mgmt"] = "wpa-psk";
  connection["802-11-wireless-security"]["pairwise"] = QStringList("ccmp");
  connection["802-11-wireless-security"]["proto"] = QStringList("rsn");
  connection["802-11-wireless-security"]["psk"] = defaultTetheringPassword;

  connection["ipv4"]["method"] = "shared";
  QMap<QString,QVariant> address;
  address["address"] = "192.168.43.1";
  address["prefix"] = 24u;
  connection["ipv4"]["address-data"] = QVariant::fromValue(IpConfig() << address);
  connection["ipv4"]["gateway"] = "192.168.43.1";
  connection["ipv4"]["route-metric"] = 1100;
  connection["ipv6"]["method"] = "ignore";

  QDBusInterface nm_settings(NM_DBUS_SERVICE, NM_DBUS_PATH_SETTINGS, NM_DBUS_INTERFACE_SETTINGS, bus);
  nm_settings.setTimeout(DBUS_TIMEOUT);
  nm_settings.call("AddConnection", QVariant::fromValue(connection));
}