%VTOL Vision Initial Sizing - Aer E 461
clear,clc,close all

%STATICS
M_p = (34.6 + 280 + 5*4 +22*2 + 75)/1000; %kg
e = 0.7; %dim, rectangle wing
a = 343; %m/s
t_c = .12; %thickness / chord for NACA4412
Q_wing = 1.25; %dim, assuming high mounted
sweep = 0;
g = 9.81;

%Flight Conditions
mu = 1.789*10^-5; %Pa*s
rho = 1.225; %kg/m^3

%Adjustables
M_craft_lb = 2.26796; %kgs
velocity_mph = 35; %mph
chord_in = 8; %inches
span_in = 30; %inches
fuse_len_in = 15; %in
fuse_diam_in = 6; %in


%Derived
velocity = velocity_mph * 0.44704; % m/s
M_craft = M_craft_lb * 0.453592; % kgs
chord = chord_in * 0.0254; %meters
span = span_in * 0.0254; %meters
fuse_len = fuse_len_in * 0.0254; %meters
fuse_diam = fuse_diam_in * 0.0254; %meters
M_tot = M_p + M_craft; % kgs
W_tot = M_tot * g; %N
wing_area = chord*span; %m^2
Reynolds = rho * velocity * chord / mu; %dim
dynamic_p = .5 * rho * velocity.^2; %Pa
AR = span^2/wing_area; %dim
M = velocity/a; %dim
Reynolds_fuse = rho * velocity * fuse_len / mu; %dim




%Friction
Cf_wing = .455./(log10(Reynolds).^2.58*(1+.144*(.06).^2).^.65);
FF_wing = (1+.6/(chord/4)*t_c+100*t_c^4)*(1.34*M.^.18*(cos(sweep))^.28);
S_wetwing = (1.977+.52*t_c)*wing_area;
S_ratio = S_wetwing/wing_area;
C_D_0_wing = S_ratio.*Q_wing.*FF_wing.*Cf_wing;
Cf_wing = .455./(log10(Reynolds_fuse).^2.58*(1+.144*(.06).^2).^.65);
f_wing = fuse_len/fuse_diam;
FF_fuse = 0.9+5/f_wing^1.5+f_wing/400;
S_wet_fuse = fuse_diam * fuse_len * pi + pi/4 * fuse_diam^2;
S_rat_fuse = S_wet_fuse/wing_area;
C_D_0_fuse = Cf_wing*FF_fuse*1*S_rat_fuse;

%Lift
CL = W_tot./(dynamic_p*wing_area);
CL_Fixed = 0.4;
e0=1.78*(1-.045*(AR.^.68))-.64;
K = 1/(pi*e0*AR); %dim
CD = C_D_0_wing+C_D_0_fuse+K*CL_Fixed.^2;
CL_CD = CL_Fixed/CD;
%Prints

fprintf("With no tail for skin drag\n  CD is: %1.4f \n",CD)
fprintf("  CL/CD is: %1.4f \n",CL_CD)
