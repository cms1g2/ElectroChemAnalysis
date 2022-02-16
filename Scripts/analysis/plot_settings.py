from matplotlib.ticker import AutoMinorLocator
from matplotlib.patches import Polygon

colours = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
def single_line_plot_settings(plot1, single_x_plot, single_y_plot, x, y, sheet):
    plot1.plot(single_x_plot,  single_y_plot, label=sheet)
    plot1.set_xlabel(x)
    plot1.set_ylabel(y)
    plot1.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left',  frameon=False)
    plot1.grid(axis="x", color="black", alpha=.5, linewidth=0.5, linestyle=":")
    plot1.grid(axis="y", color="black", alpha=.5, linewidth=0.5, linestyle=":")
    plot1.xaxis.set_minor_locator(AutoMinorLocator())
    plot1.yaxis.set_minor_locator(AutoMinorLocator())
    plot1.tick_params(which='minor', direction='in', top=True, right=True)
    plot1.tick_params(direction='in', top=True, right=True)

def colour_by_z_scatter(plot1, fig, x_plot, y_plot, z_plot, x, y, sheet):
    scatt = plot1.scatter(x_plot, y_plot, c = z_plot, cmap='coolwarm')
    plot1.set_xlabel(x)
    plot1.set_ylabel(y)
    fig.colorbar(scatt, ax=plot1, label='Scans')
    plot1.set_title(sheet)
    plot1.tick_params(direction='in', top=True, right=True)
    plot1.grid(axis="x", color="black", alpha=.5, linewidth=0.5, linestyle=":")
    plot1.grid(axis="y", color="black", alpha=.5, linewidth=0.5, linestyle=":")
    plot1.xaxis.set_minor_locator(AutoMinorLocator())
    plot1.yaxis.set_minor_locator(AutoMinorLocator())

def scatter_plot(plot1, x_plot, y_plot, x, y, sheet):
    plot1.scatter(x_plot, y_plot, label=sheet)
    plot1.set_xlabel(x)
    plot1.set_ylabel(y)
    plot1.legend(bbox_to_anchor=(2.0, 1.0), loc='upper left',  frameon=False)
    plot1.tick_params(direction='in', top=True, right=True)
    plot1.grid(axis="x", color="black", alpha=.5, linewidth=0.5, linestyle=":")
    plot1.grid(axis="y", color="black", alpha=.5, linewidth=0.5, linestyle=":")
    plot1.xaxis.set_minor_locator(AutoMinorLocator())
    plot1.yaxis.set_minor_locator(AutoMinorLocator())

def plot_2_scans(plot1,x_1_plot, y_1_plot, x_2_plot, y_2_plot, x, y, sheet, col):
    plot1.plot(x_1_plot,  y_1_plot,  label='1st '+sheet, c=colours[col])
    plot1.plot(x_2_plot,  y_2_plot, linestyle='--', dashes=(3, 5),  label='2nd '+sheet, c=colours[col])
    plot1.set_xlabel(x)
    plot1.set_ylabel(y)
    plot1.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left',  frameon=False)
    plot1.grid(axis="x", color="black", alpha=.5, linewidth=0.5, linestyle=":")
    plot1.grid(axis="y", color="black", alpha=.5, linewidth=0.5, linestyle=":")
    plot1.xaxis.set_minor_locator(AutoMinorLocator())
    plot1.yaxis.set_minor_locator(AutoMinorLocator())
    plot1.tick_params(which='minor', direction='in', top=True, right=True)
    plot1.tick_params(direction='in', top=True, right=True)

def plt_2_scans_single(plot1,x_plot, y_plot, x, y, sheet, col):
    plot1.plot(x_plot,  y_plot,  label='1st '+sheet, c=colours[col+1])
    plot1.set_xlabel(x)
    plot1.set_ylabel(y)
    plot1.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left',  frameon=False)
    plot1.tick_params(direction='in', top=True, right=True)
    plot1.grid(axis="x", color="black", alpha=.5, linewidth=0.5, linestyle=":")
    plot1.grid(axis="y", color="black", alpha=.5, linewidth=0.5, linestyle=":")
    plot1.xaxis.set_minor_locator(AutoMinorLocator())
    plot1.yaxis.set_minor_locator(AutoMinorLocator())
    plot1.tick_params(which='minor', direction='in', top=True, right=True)

def integrate_data_plot(ax, single_x_scan_2, single_y_scan, x, y):
    ax.plot(single_x_scan_2, single_y_scan)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.ticklabel_format(useOffset=False, style='plain')
    ax.grid(axis="x", color="black", alpha=.5, linewidth=0.5, linestyle=":")
    ax.grid(axis="y", color="black", alpha=.5, linewidth=0.5, linestyle=":")
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which='minor', direction='in', top=True, right=True)
    ax.tick_params(direction='in', top=True, right=True)

def integation_plot(ax, inter_x_1, inter_x_2, inter_y_1, inter_y_2, new_x_3, new_y_3):
    marker_x = [inter_x_1, inter_x_2]
    marker_y = [inter_y_1, inter_y_2]
    ax.scatter(marker_x, marker_y, s=200, marker="|")
    verts_2 = [(inter_x_1, inter_y_1), *zip(new_x_3, new_y_3), (inter_x_2, inter_y_2)]
    poly_2 = Polygon(verts_2, facecolor='0.9', edgecolor='0.5')
    ax.add_patch(poly_2)