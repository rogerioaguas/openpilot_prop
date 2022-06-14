export OSM_DIR=/data/osm
export DB_DIR=${OSM_DIR}/db
export GZ_MAP_FILE_NAME=south-america/brazil-latest.osm.bz2
export GZ_MAP_FILE=${OSM_DIR}/${GZ_MAP_FILE_NAME}

# Remove legacy compressed map file if existing
[ -f $GZ_MAP_FILE ] && rm -rf $GZ_MAP_FILE

# WD
cd $OSM_DIR

# Download map file
wget https://download.geofabrik.de/south-america/brazil-latest.osm.bz2

if [[ "$?" != 0 ]]; then
  echo "Error downloading map file"
else
  echo "Successfuly downloaded map file"
  # Remove current db dir if exisiting
  [ -f $DB_DIR ] && rm -rf $DB_DIR
  # Uncompress
  nohup ../src/bin/init_osm3s.sh brazil-latest.osm.bz2 $DB_DIR $EXEC_DIR --meta & tail -f nohup.out
  # Remove compressed map files after expanding
  rm -rf brazil-latest.osm.bz2
fi
