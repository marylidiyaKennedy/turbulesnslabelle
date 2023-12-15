uiopen('/home/amurali/Desktop/Sergey/GPANNpaper/Original_space/St_0_5/220308_SP7_spod_m0_St05_NORM_M50G50_Strat15_a4_1e-2_a8_1e-1_a10_0_R3G50_FFT_Test.fig',1)

fig=gca;
xdata2 = fig.Children(1).XData;
ydata2 = fig.Children(1).YData;

data = [xdata2' ydata2'];

csvwrite('HyGP_psd.csv', data);

xdata3 = fig.Children(2).XData;
ydata3 = fig.Children(2).YData;

data = [xdata3' ydata3'];

csvwrite('True_psd.csv', data);
