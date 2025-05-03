import matplotlib.pyplot as plt
import numpy as np

def translation(x,y):
    tx=int(input("Enter translation in x direction: "))
    ty=int(input("Enter translation in y direction: "))
    x_translated=[x[i]+ tx for i in range(len(x))]
    y_translated=[y[i]+ ty for i in range(len(x))]
    return x_translated,y_translated

def scaling(x,y):
    sx=float(input("Enter sclaing factor in x direction: "))
    sy=float(input("Enter scaling factor in y direction: "))
    x_scaled=[(x[i]*sx) for i in range(len(x))]
    y_scaled=[(y[i]*sy) for i in range(len(y))]
    return x_scaled,y_scaled,sx,sy 

def rotation(x,y):
    angle=int(input("Enter angle of rotation: "))
    angle_radians = np.radians(angle)
    x_rotated = [(x[i] * np.cos(angle_radians) - y[i] * np.sin(angle_radians)) for i in range(len(x))]
    y_rotated = [(x[i] * np.sin(angle_radians) + y[i] * np.cos(angle_radians)) for i in range(len(x))]
    return x_rotated,y_rotated,angle

def reflection(x,y):
    print("Select the axis of Reflection:")
    print("1. X-axis")
    print("2. Y-axis")
    print("3. Origin")
    ch= int(input("Enter your choice: "))
    if ch == 1:
        x_reflected=x
        y_reflected=[-y[i] for i in range(len(x))]
    elif ch == 2:
        x_reflected=[-x[i] for i in range(len(x))]
        y_reflected=y
    elif ch == 3:
        x_reflected=[-x[i] for i in range(len(x))]
        y_reflected=[-y[i] for i in range(len(x))]
    else:
        print("Invalid ch. Please try agian.")
        return reflection(x,y)
    return x_reflected,y_reflected,ch

def shearing(x,y):
    shx=float(input("Enter shearing factor in x direction: "))
    shy= float(input("Enter shearing factor in y direction: "))
    x_sheared=[(x[i]+shx*y[i]) for i in range(len(x))]
    y_sheared=[(y[i]+shy*x[i]) for i in range(len(x))]
    return x_sheared,y_sheared,shx,shy

def plotting(x,y,x_values,y_values,choice,angle=None,ch=None,scle_x=None, scle_y=None, shx=None,shy=None,n=None):
    fig, axes = plt.subplots(1, 2, figsize=(16, 9))
    plt.get_current_fig_manager().window.state('zoomed')
    if(n==2):
        shape_type = "Line"
    elif(n==3):
        shape_type= "Triangle"
    elif(n==4):
        shape_type= "Quadrilateral"
    elif(n>4):
        shape_type= "Polygon"
    ax1,ax2=axes.flatten()
    ax1.plot(x,y,marker='o')

    ax1.set_title(f"Original {shape_type}")
    ax1.set_xlim(np.min(np.concatenate((x,x_values)))-2,np.max(np.concatenate((x,x_values)))+2)
    ax1.set_ylim(np.min(np.concatenate((y,y_values)))-2,np.max(np.concatenate((y,y_values)))+2)
    ax1.grid(True, linestyle='--', alpha=0.5) 
    ax1.axhline(0, color='black', linewidth=1.5)  
    ax1.axvline(0, color='black', linewidth=1.5)  
    for i in range(len(x)-1):
        ax1.text(x[i], y[i], f" ({x[i]:.2f}, {y[i]:.2f})", fontsize=10, color='blue')
    
    ax2.plot(x_values,y_values,marker='o', color='red')
    if choice==1:
        ax2.set_title(f"Translated {shape_type} by ({x_values[0]-x[0]}, {y_values[0]-y[0]})")
    elif choice==2:
        ax2.set_title(f"Scaled {shape_type} by ({scle_x}, {scle_y})")

    elif choice==3:
        ax2.set_title(f"Rotated {shape_type} by {angle} degrees")
    elif choice==4:
        if ch == 1:
            ax2.set_title(f"Reflected {shape_type} across X-axis")
        elif ch == 2:
            ax2.set_title(f"Reflected {shape_type} across Y-axis")
        elif ch == 3:
            ax2.set_title(f"Reflected {shape_type} across Origin")
    elif choice==5:
        ax2.set_title(f"Sheared {shape_type} by ({shx}, {shy})")
    ax2.set_xlim(np.min(np.concatenate((x,x_values)))-2,np.max(np.concatenate((x,x_values)))+2)
    ax2.set_ylim(np.min(np.concatenate((y,y_values)))-2,np.max(np.concatenate((y,y_values)))+2)
    ax2.grid(True, linestyle='--', alpha=0.5)  
    ax2.axhline(0, color='black', linewidth=1.5) 
    ax2.axvline(0, color='black', linewidth=1.5)  
    for i in range(len(x)-1):
        ax2.text(x_values[i], y_values[i], f" ({x_values[i]:.2f}, {y_values[i]:.2f})", fontsize=10, color='red')
    plt.show()

x=[]
y=[]
n=int(input("Enter number of vertices: "))
for i in range(n):
    x.append(float(input(f"x[{i}]: ")))
    y.append(float(input(f"y[{i}]: ")))
x.append(x[0])
y.append(y[0])

while True:
    print("Select your Choice.")
    print("1. Translation")
    print("2. Scaling")
    print("3. Rotation")
    print("4. Reflection")
    print("5. Shearing")
    print("6. Exit")
    choice= int(input("Enter your choice: "))
    if(choice==1):
        x_values,y_values= translation(x,y)
        x_values = np.array(x_values, dtype=float)
        y_values = np.array(y_values, dtype=float)
        plotting(x,y,x_values,y_values,choice,n=n)

    elif(choice==2):
        x_values,y_values,scle_x,scle_y= scaling(x,y)
        x_values = np.array(x_values, dtype=float)
        y_values = np.array(y_values, dtype=float)
        plotting(x,y,x_values,y_values,choice, scle_x=scle_x,scle_y=scle_y, n=n)
        
    elif(choice==3):
        x_values,y_values,angle=rotation(x,y)
        x_values=np.array(x_values,dtype=float)
        y_values=np.array(y_values,dtype=float)
        plotting(x,y,x_values,y_values,choice,angle,n=n)

    elif(choice==4):
        x_values,y_values,ch=reflection(x,y)
        x_values=np.array(x_values,dtype=float)
        y_values=np.array(y_values,dtype=float)
        plotting(x,y,x_values,y_values,choice,ch=ch,n=n)
    elif(choice==5):
        x_values,y_values,shx,shy=shearing(x,y)
        x_values=np.array(x_values,dtype=float)
        y_values=np.array(y_values,dtype=float)
        plotting(x,y,x_values,y_values,choice,shx=shx, shy=shy,n=n)
    elif(choice==6):
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
        continue
    cont = input("Do you want to perform another operation? (y/n): ")
    if cont.strip().lower() != 'y':
        print("Thank you for using the program.!")
        break
