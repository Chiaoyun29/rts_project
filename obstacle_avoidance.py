from controller import Robot

# get the time step of the current world.
TIMESTEP = 1
MAX_SPEED = 6.28 #can check from scene tree

def run_robot():
    # create the Robot instance.
    robot = Robot()

    # Get the instance of a device of the robot.
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    # ir0 = robot.getDevice('ps0')
    # ir0.enable(TIMESTEP)
    list_ps = []
    for ind in [0, 1, 2, 5, 6, 7]:
        sensor_name = 'ps' + str(ind)
        list_ps.append(robot.getDevice(sensor_name))
        list_ps[-1].enable(TIMESTEP)

    # Main loop:
    while robot.step(TIMESTEP) != -1:
        left_speed = MAX_SPEED
        right_speed = MAX_SPEED
        # Read the sensors and process sensor data here.
        #val = ir0.getValue()
        for ps in list_ps:
            ps_val=ps.getValue()
            print(ps_val)
            if ps_val>80:
                left_speed = -MAX_SPEED
        
        # Then, send actuator commands.
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

if __name__ == "__main__":
    run_robot()  # No arguments passed here.

