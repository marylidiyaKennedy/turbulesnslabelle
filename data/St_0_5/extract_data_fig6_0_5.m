uiopen('/home/amurali/Desktop/Sergey/GPANNpaper/Original_space/St_0_5/220308_SP7_spod_m0_St05_NORM_M50G50_Strat15_a4_1e-2_a8_1e-1_a10_0_R3G50_TEST.fig',1)
fig=gca;
xdata2 = fig.Children(2).XData;
ydata2 = fig.Children(2).YData;

data = [xdata2' ydata2'];

csvwrite('HyGP.csv', data);

xdata3 = fig.Children(3).XData;
ydata3 = fig.Children(3).YData;

data = [xdata3' ydata3'];

csvwrite('True.csv', data);
