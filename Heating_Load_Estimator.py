import matplotlib.pyplot as plt             # for plotting the variables
from matplotlib import cm                   # for creating a colormap
from matplotlib.ticker import LinearLocator # to create tickers in the plots
import matplotlib.animation as animation    # to create and save an anima..
from matplotlib.animation import FuncAnimation # specific animation package
import numpy as np                          # for handling the numbers
from mpl_toolkits import mplot3d            # for creating a 3d plot
from IPython.display import display, clear_output
                                            # to see a nice anima. in the notebook environment

x0 = 0                                     # the initial point in space domian
x_max = 1                                  # the final foint in the space domian
nx = 20                                    # the number of points in the space discretization

t0 = 0                                     # initil time
t_max=15                                   # final simulation time
nt = 1000                                  # number of time steps


def stability_check(dt, dx, alpha):
    """
    The function checks the stability of the explicit scheme by estimating is dt*alpha/dx^2 is less than 0.5 for the choice of \
    space and time discretization
    """
    F = (dt / np.power(dx, 2)) * alpha
    assert F < 0.5
    return F

def init_space(x0, x_max,nx):
    """
    Generates the space domain for simulation
    """
    dx = (x_max-x0)/nx
    x = np.linspace(x0,x_max,nx)
    return dx, x

def init_time(t0, t_max,nt):
    "generates the time domain for simulation"
    dt = (t_max-t0)/nt
    t = np.linspace(t0,t_max,nt)
    return dt, t

def set_field(nx,nt):
    "Genrates a two dimensional field for the variable in space and time"
    p = np.zeros(shape=(nx,nt))
    return p

pi=1     # 1 MPa
def set_ic(pi):
    """
    This gives a very simplistic initial condition
    """
    p = np.zeros(shape=(nx, nt))
    p.fill(pi)
    return p

def set_bc(p0,pL):
    """
    constant boundary condition is set using this function
    """
    p = np.zeros(shape=(nx, nt))
    p[0,:]=p0
    p[nx-1,:]=pL
    return p[0,:], p[nx-1,:]

def FDM_1D(p, nx, nt, F):
    """
    The function runs a loop utilizing explicit marching in time.
    """
    j=0;i=0
    for i in range(0,nt-1):
        for j in range(1,nx-1):
            p[j,i+1] = ((F)*(p[j+1,i]-2*p[j,i]+p[j-1,i])+p[j,i])
    return p


# Executing the written functions in order

dx, x = init_space(x0, x_max, nx)
dt, t = init_time(t0, t_max, nt)
F = stability_check(dt, dx,alpha=1)
p = set_field(nx, nt)
# p = set_ic(pi)
p[0, :], p[nx - 1, :] = set_bc(2, 0)
p = FDM_1D(p, nx, nt, F)

# -------------------------Information to be printed after simulation-------------
print("Simulation Message: \n\nThe space domain is set between:", x0, "and", x_max, " unit and the simulation time \
is set for a t max of: ", t_max, "sec.\nThe value of space increment is:", dx,
      "unit and the value of time increment is:", dt, "sec\n\n" 
                                                      "Checked the stability condition for explicit scheme,\n\
                                                The value of F is:", np.round(F, 2), "for stability of the Explicit solution to work,\
the value of F should be less than 0.5")

assert p.shape[0] == x.shape[0] and p.shape[1] == t.shape[0], f"The shape of p and x does not match: {p.shape[1]}"

# Plotting the solution in 2-D
x, t = np.meshgrid(x, t)

fig, axs = plt.subplots(1,1,figsize=(15,10),subplot_kw={"projection":'3d'})
surf=axs.plot_surface(x, t, np.transpose(p),cmap='seismic', edgecolor='none')
# Customize the z axis.
axs.set_zlim(0, 4)
axs.zaxis.set_major_locator(LinearLocator(5))
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
axs.set_xlabel('Length (m)')
axs.set_ylabel('Time (sec)')
axs.set_zlabel('Pressure (MPa)')
axs.set_title('surface')
plt.savefig("1D Pressure Diffusion.jpeg")

# Plotting the simulation of changes in pressure with time (Animation)

dx, x = init_space(x0, x_max, nx)
pt = np.transpose(p)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
# add another axes at the top left corner of the figure
axtext = fig.add_axes([0.0, 0.95, 0.1, 0.05])
# turn the axis labels/spines/ticks off
axtext.axis("off")

ax1.set_ylabel("Pressure, MPa")
ax1.set_xlabel("Length, m")
ax1.set_title("1D Diffusion Simulation")
timeer = ax1.annotate("Timer", xy=(0.8, 2), xytext=(0.5, 2))
time = ax1.annotate(0, xy=(0.6, 2), xytext=(0.6, 2))
l, = ax1.plot(x[:], p[:, 0], "r--", lw=4)


# animate = lambda i: l.set_ydata(p[:,i]); time.set_text(i);

def animate(i):
    l.set_ydata(p[:, i])
    time.set_text(i)
    return l, time


for i in range(p.shape[1] - 800):
    animate(i)
    clear_output(wait=True)
    display(fig)