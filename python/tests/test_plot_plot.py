import pytest
from .context import enkf_seir
from enkf_seir import plot
from enkf_seir.plot import tecplot_loader
from enkf_seir.plot import plot

import os
import sys
from pathlib import Path

def test_enkf_seir_plot_plot(tmp_path):
    obs = '''TITLE = "Observations"
 VARIABLES = "i" "time" "ave" "std" 
 ZONE T="Observed deaths"  F=POINT, I=   4, J=1, K=1
    1   12      1.0000      2.0000
    2   13      1.0000      2.0000
    3   14      3.0000      2.0000
    4   15      3.0000      2.0000
'''
    file = tmp_path / "obs.dat"
    file.write_text(obs)

    dead_0 = '''TITLE = "Dead_0"
VARIABLES = "time" "ave" "std" 
 "   1" "   2" "   3" "   4" "   5" "   6" "   7" "   8" "   9" "  10"
 ZONE T="Dead_0"  F=POINT, I=         10 , J=1, K=1
 0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00
 0.10000E+01  0.85718E-03  0.26165E-03  0.14736E-02  0.80208E-03  0.10249E-02  0.77432E-03  0.57612E-03
 0.20000E+01  0.39479E-02  0.10594E-02  0.60711E-02  0.38385E-02  0.43267E-02  0.38423E-02  0.29940E-02
 0.30000E+01  0.12354E-01  0.30952E-02  0.18113E-01  0.12325E-01  0.13168E-01  0.12388E-01  0.97958E-02
 0.40000E+01  0.28152E-01  0.68930E-02  0.38551E-01  0.28608E-01  0.28823E-01  0.28542E-01  0.23068E-01
 0.50000E+01  0.54593E-01  0.13309E-01  0.77054E-01  0.55192E-01  0.57959E-01  0.54324E-01  0.45448E-01
 0.60000E+01  0.94353E-01  0.23057E-01  0.13051E+00  0.96361E-01  0.10002E+00  0.92983E-01  0.79617E-01
 0.70000E+01  0.15126E+00  0.37552E-01  0.20661E+00  0.15596E+00  0.16149E+00  0.14777E+00  0.12788E+00
 0.80000E+01  0.22997E+00  0.58537E-01  0.31251E+00  0.23800E+00  0.24912E+00  0.22121E+00  0.19407E+00
 0.90000E+01  0.33604E+00  0.88732E-01  0.45640E+00  0.34742E+00  0.37120E+00  0.31598E+00  0.28291E+00
'''
    file = tmp_path / "dead_0.dat"
    file.write_text(dead_0)

    dead_1 = '''TITLE = "Dead_1"
VARIABLES = "time" "ave" "std" 
 "   1" "   2" "   3" "   4" "   5" "   6" "   7" "   8" "   9" "  10"
 ZONE T="Dead_1"  F=POINT, I=         10 , J=1, K=1
  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00 
  0.10000E+01  0.46713E-03  0.11514E-03  0.83621E-03  0.49238E-03  0.45006E-03  0.47028E-03  0.48202E-03 
  0.20000E+01  0.24210E-02  0.43353E-03  0.36989E-02  0.26307E-02  0.22909E-02  0.27718E-02  0.26908E-02 
  0.30000E+01  0.79619E-02  0.13238E-02  0.11685E-01  0.86289E-02  0.75738E-02  0.92491E-02  0.87377E-02 
  0.40000E+01  0.18714E-01  0.29867E-02  0.26468E-01  0.20242E-01  0.17877E-01  0.22101E-01  0.21386E-01 
  0.50000E+01  0.36997E-01  0.57547E-02  0.51055E-01  0.40140E-01  0.35185E-01  0.44835E-01  0.42027E-01 
  0.60000E+01  0.65475E-01  0.98471E-02  0.87388E-01  0.71185E-01  0.62448E-01  0.78746E-01  0.74261E-01 
  0.70000E+01  0.10769E+00  0.15662E-01  0.14009E+00  0.11720E+00  0.10313E+00  0.12857E+00  0.12170E+00 
  0.80000E+01  0.16772E+00  0.23539E-01  0.21631E+00  0.18167E+00  0.16083E+00  0.19939E+00  0.18905E+00 
  0.90000E+01  0.25112E+00  0.33926E-01  0.32085E+00  0.27070E+00  0.24031E+00  0.29740E+00  0.28301E+00 
'''
    file = tmp_path / "dead_1.dat"
    file.write_text(dead_1)

    data_dir = tmp_path
    requested_vars = ['dead'] 
    figs_out_dir = data_dir
    format = 'png'
    dpi = 300
    prior = 'false'
    show = 'false'
    t0 = None
    tf = None
    daily = 'false'
    enkf_seir.plot.plot.plot_save_variables(data_dir, requested_vars, figs_out_dir, format, dpi, prior, show, t0, tf, daily)


    assert Path(tmp_path / 'dead.png').is_file()
