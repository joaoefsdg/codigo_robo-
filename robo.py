import wpilib
import wpilib.drive
import clre

class Myrobot (wpilib.TimedRobot):
    def robotinit (self):
        # os 4 motores da traçao 
        self.m_left_front = ctre.WPI_VictorSPX(22)
        self.m_right_front = ctre.WPI_VictorSPX(33)
        self.a_left_rear = ctre.WPI_VictorSPX(11)
        self.m_right_rear = ctre.WPI_VictorSPX(44)
        # motores dos mecanismos
        self.shooter = ctre.WPI_VictorSPX(9)
        self.track_ball = ctre.WPI_VictorSPX(8)
        self.ball_catcher = ctre.WPI_VictorSPX(55)
        # lado esquerdo e lado direito da trçao
        self.m_Left = wpilib.SpeadControllerGroup (self.m.left_front,self.m_left_rear)
        self.m_right = wpilib.SpeadControllerGroup (self.m.left_front,self.m_left_rear)
        # criando a traçao como um objeto
        self.myRobot = wpilib.drive.DiferentialDrive(self.m_left,self,se)
        self.myRobot.setExpiration(0,1)
        # criando um joistick
        self.stick = wpilib.joistick(0)
        # criar uma camera
        wpili.Cameraserver.launch(*vision.py:main*)
        # criando um relogio para contar o tempo
        self.timer = wpilib.Timer()
# criando o teleoperando
def telepInit(self):
    self. myRobot.setSafetyEnabled(True)

# criar o periodo teleoperando 
def teleopPeriodic(self):
    if self.stick.getRawButton(5)   == True:
        self.myRobot.arcadeDrive(
            -self.stick.getRawaxis(1) , self.stick.getRawaxis(0)*1.15,True
        )
    else:
        self.myRobot.arcadeDrive(
            self.stickgetRAwAxis(1),self.stick.getRawAxis(0)*1.15,True
        )
        