#!/usr/bin/env python3
from enum import Enum


class LongTunes(Enum):
  PEDAL = 0
  TSS2 = 1
  TSS = 2

class LatTunes(Enum):
  INDI_PRIUS = 0
  LQR_RAV4 = 1
  PID_A = 2
  PID_B = 3
  PID_C = 4
  PID_D = 5
  PID_E = 6
  PID_F = 7
  PID_G = 8
  PID_I = 9
  PID_H = 10
  PID_J = 11
  PID_K = 12
  PID_L = 13
  PID_M = 14
  PID_N = 15
  INDI_COROLLAS_TSS2 = 16


###### LONG ######
def set_long_tune(tune, name):
  # Improved longitudinal tune
  if name == LongTunes.TSS2 or name == LongTunes.PEDAL:
    tune.deadzoneBP = [0., 8.05]
    tune.deadzoneV = [.0, .14]
    tune.kpBP = [0., 5., 20.]
    tune.kpV = [.9, .6, 0.375]
    tune.kiBP = [0., 5., 12., 20., 27.]
    tune.kiV = [.27, .20, .18, .17, .1]
  # Default longitudinal tune
  elif name == LongTunes.TSS:
    tune.deadzoneBP = [0., 9.]
    tune.deadzoneV = [0., .15]
    tune.kpBP = [0., 5., 35.]
    tune.kiBP = [0., 35.]
    tune.kpV = [.9, .6, .375]
    tune.kiV = [0.27, 0.18]
  else:
    raise NotImplementedError('This longitudinal tune does not exist')


###### LAT ######
def set_lat_tune(tune, name):
  if name == LatTunes.INDI_PRIUS:
    tune.init('indi')
    tune.indi.innerLoopGainBP = [0.]
    tune.indi.innerLoopGainV = [4.0]
    tune.indi.outerLoopGainBP = [0.]
    tune.indi.outerLoopGainV = [3.0]
    tune.indi.timeConstantBP = [0.]
    tune.indi.timeConstantV = [0.1]
    tune.indi.actuatorEffectivenessBP = [0.]
    tune.indi.actuatorEffectivenessV = [1.0]

  # birdman6450#7399's Corolla 2020 TSS2 Tune
  elif name == LatTunes.INDI_COROLLAS_TSS2:
    tune.init('indi')
    tune.indi.innerLoopGainBP = [18, 22, 26]
    tune.indi.innerLoopGainV = [9, 12, 15]
    tune.indi.outerLoopGainBP = [18, 22, 26]
    tune.indi.outerLoopGainV = [8, 11, 14.99]
    tune.indi.timeConstantBP = [18, 22, 26]
    tune.indi.timeConstantV = [1, 3, 4.5]
    tune.indi.actuatorEffectivenessBP = [18, 22, 26]
    tune.indi.actuatorEffectivenessV = [9, 12, 15]

  elif name == LatTunes.LQR_RAV4:
    tune.init('lqr')
    tune.lqr.scale = 1500.0
    tune.lqr.ki = 0.05
    tune.lqr.a = [0., 1., -0.22619643, 1.21822268]
    tune.lqr.b = [-1.92006585e-04, 3.95603032e-05]
    tune.lqr.c = [1., 0.]
    tune.lqr.k = [-110.73572306, 451.22718255]
    tune.lqr.l = [0.3233671, 0.3185757]
    tune.lqr.dcGain = 0.002237852961363602

  elif 'PID' in str(name):
    tune.init('pid')
    tune.pid.kiBP = [0.0]
    tune.pid.kpBP = [0.0]
    if name == LatTunes.PID_A:
      tune.pid.kpV = [0.2]
      tune.pid.kiV = [0.05]
      tune.pid.kf = 0.00003
    elif name == LatTunes.PID_B:
      tune.pid.kpV = [0.6]
      tune.pid.kiV = [0.05]
      tune.pid.kf = 0.00006
    elif name == LatTunes.PID_C:
      tune.pid.kpV = [0.6]
      tune.pid.kiV = [0.1]
      tune.pid.kf = 0.00006
    elif name == LatTunes.PID_D:
      tune.pid.kpV = [0.6]
      tune.pid.kiV = [0.1]
      tune.pid.kf = 0.00007818594
    elif name == LatTunes.PID_E:
      tune.pid.kpV = [0.6]
      tune.pid.kiV = [0.15]
      tune.pid.kf = 0.00007818594
    elif name == LatTunes.PID_F:
      tune.pid.kpV = [0.723]
      tune.pid.kiV = [0.0428]
      tune.pid.kf = 0.00006
    elif name == LatTunes.PID_G:
      tune.pid.kpV = [0.18]
      tune.pid.kiV = [0.015]
      tune.pid.kf = 0.00012
    elif name == LatTunes.PID_H:
      tune.pid.kpV = [0.17]
      tune.pid.kiV = [0.03]
      tune.pid.kf = 0.00006
    elif name == LatTunes.PID_I:
      tune.pid.kpV = [0.15]
      tune.pid.kiV = [0.05]
      tune.pid.kf = 0.00004
    elif name == LatTunes.PID_J:
      tune.pid.kpV = [0.19]
      tune.pid.kiV = [0.02]
      tune.pid.kf = 0.00007818594
    elif name == LatTunes.PID_L:
      tune.pid.kpV = [0.3]
      tune.pid.kiV = [0.05]
      tune.pid.kf = 0.00006
    elif name == LatTunes.PID_M:
      tune.pid.kpV = [0.3]
      tune.pid.kiV = [0.05]
      tune.pid.kf = 0.00007
    elif name == LatTunes.PID_N:
      tune.pid.kpV = [0.35]
      tune.pid.kiV = [0.15]
      tune.pid.kf = 0.00007818594
    else:
      raise NotImplementedError('This PID tune does not exist')
  else:
    raise NotImplementedError('This lateral tune does not exist')