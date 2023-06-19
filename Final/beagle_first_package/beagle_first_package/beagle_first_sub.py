import rclpy as rp
from rclpy.node import Node
from roboid import *
import roboidai as ai
from std_msgs.msg import String
import time
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from beagle_msgs.action import Distbeagle
from std_msgs.msg import Float64
from rclpy.executors import MultiThreadedExecutor # 콜백 함수 병렬 처리용 
from rclpy.callback_groups import ReentrantCallbackGroup # 콜백 함수 병렬 처리용 
import argparse # 실행 인자 사용 시 필요
import sys # 실행 인자 사용 시 필요
from rcl_interfaces.msg import SetParametersResult # 파라미터 사용시 필요
from rclpy.parameter import Parameter # 파라미터 사용시 필요

beagle  = Beagle()
timer_bucket = 0
end_game = 1                        # 1이면 일반 모드, 2면 멸망전; 주사위 눈 수 x2
wheel_pulse = 1440
wheel_speed = 15*end_game

beagle.start_lidar()
beagle.wait_until_lidar_ready()
beagle.lidar_chart()
print('Lidar Starts')


class direct_mode_sub(Node) :
     def __init__(self) :
          super().__init__('beagle_first_subscriber')
          self.callback_group = ReentrantCallbackGroup() # 콜백 함수 병렬 처리용 
          self.subscription = self.create_subscription( # 서브스크라이버
               String,
               'topic',
               self.listner_callback,
               10,
               callback_group=self.callback_group # 콜백 함수 병렬 처리용 
               )
          self.subscription
          
          self._action_server = ActionServer( # 액션 서버
               self,
               Distbeagle,
               'distbeagle',
               self.execute_callback,
               callback_group = self.callback_group ) # 콜백 함수 병렬 처리용 
        
          self.current_distance = 0.0

          self.declare_parameter('end_game', 1) # 파라미터
          self.end_game = end_game
          self.wheel_speed = wheel_speed
          self.end_game = self.get_parameter('end_game').value
          self.add_on_set_parameters_callback(self.update_parameter) # 업데이트 된 파라미터 가져오기
          
         

     def listner_callback(self,msg): # 서브스크라이버의 콜백 함수
          move_point = self.load_move_point()
          if msg.data == "DICE0" :
               print("dice0")
               self.get_logger().info('Subscribing: "DICE0"')
               print("beagle stays")
               

          elif msg.data == "DICE1" :
               print("dice1")
               self.get_logger().info('Subscribing: "DICE1"')

               print("beagle go 1")
               for i in range(1*self.end_game) :
                    move_point += 1
                    beagle.move_forward_pulse(wheel_pulse, self.wheel_speed)
                    if (move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16) :
                         beagle.turn_right_pulse(705,self.wheel_speed)
                    if move_point > 16 :
                         move_point -= 16
               self.move_point = move_point

          elif msg.data == "DICE2" :
               print("DICE2")
               self.get_logger().info('Subscribing: "DICE2"')

               print("beagle go 2")
               for i in range(2*self.end_game) :
                    move_point += 1
                    beagle.move_forward_pulse(wheel_pulse, self.wheel_speed)
                    if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
                         beagle.turn_right_pulse(705,self.wheel_speed)
                    if move_point > 16 :
                         move_point -= 16
               self.move_point = move_point

          elif msg.data == "DICE3" :
               print("DICE3")
               self.get_logger().info('Subscribing: "DICE3"')

               print("beagle go 3")
               for i in range(3*self.end_game) :
                    beagle.move_forward_pulse(wheel_pulse, self.wheel_speed)
                    move_point += 1
                    if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
                         beagle.turn_right_pulse(705,self.wheel_speed)
                    if move_point > 16 :
                         move_point -= 16
               self.move_point = move_point

          elif msg.data == "DICE4" :
               print("DICE4")
               self.get_logger().info('Subscribing: "DICE4"')

               print("beagle go 4")
               for i in range(4*self.end_game) :
                    move_point += 1
                    beagle.move_forward_pulse(wheel_pulse, self.wheel_speed)
                    if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
                         beagle.turn_right_pulse(705,self.wheel_speed)
                    if move_point > 16 :
                         move_point -= 16
               self.move_point = move_point

          elif msg.data == "DICE5" :
               print("DICE5")
               self.get_logger().info('Subscribing: "DICE5"')

               print("beagle go 5")
               for i in range(5*self.end_game) :
                    beagle.move_forward_pulse(wheel_pulse, self.wheel_speed)
                    move_point += 1
                    if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
                         beagle.turn_right_pulse(705,self.wheel_speed)
                    if move_point > 16 :
                         move_point -= 16
               self.move_point = move_point

          elif msg.data == "DICE6" :
               print("DICE6")
               self.get_logger().info('Subscribing: "DICE6"')

               print("beagle go 6")
               for i in range(6*self.end_game) :
                    beagle.move_forward_pulse(wheel_pulse, self.wheel_speed)
                    move_point += 1
                    if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
                         beagle.turn_right_pulse(705,self.wheel_speed)
                    if move_point > 16 :
                         move_point -= 16
               self.move_point = move_point
          self.save_move_point(self.move_point)

     def load_move_point(self): # 비글 위치 불러오기
          try:
               with open("move_point.txt", "r") as file:
                    return int(file.read())
          except FileNotFoundError:
               return 0

     def save_move_point(self, value): # 비글 위치 저장하기
          with open("move_point.txt", "w") as file:
               file.write(str(value))


     def execute_callback(self, goal_handle): # 액션 서버의 콜백 함수

          self.get_logger().info('Executing Goal...')

          feedback_msg = Distbeagle.Feedback()
          result_msg = Distbeagle.Result()

          target_distance = goal_handle.request.target_distance

          while rp.ok():
               rear_distance = beagle.rear_lidar()
               right_distance = beagle.right_lidar()
               right_rear_distance = beagle.right_rear_lidar()
               front_distance = beagle.front_lidar()
               right_front_distance = beagle.right_front_lidar()

               if 250 <= rear_distance <= 400 or 250 <= right_distance <= 400 or 250 <= right_rear_distance <= 400:
                    beagle.sound("engine", 1)
                    print('Player is in 3 Tiles Back')
                    #time.sleep(1)

               if 60 < rear_distance < 250 or 60 < right_distance < 250 or 60 < right_rear_distance < 250:
                    beagle.sound("siren", 1)
                    print('Player is in 1 Tile Back')
                    #time.sleep(1)

               if rear_distance <= 60:
                    beagle.stop()
                    beagle.sound("sad", 1)
                    print('Player Caught the Beagle')
                    print('Beagle is the Loser..')
                    time.sleep(10)
                    beagle.dispose()
                    break

               if 250 <= front_distance <= 400 or 250 <= right_front_distance <= 400:
                    beagle.sound("march", 1)
                    print('Player is in 3 Tiles Forward')
                    #time.sleep(1)

               if 60 < front_distance < 250 or 60 < right_front_distance < 250:
                    beagle.sound("good job", 1)
                    print('Player is in 1 Tile Forward')
                    #time.sleep(1)

               if front_distance <= 60:
                    beagle.stop()
                    beagle.sound("happy", 1)
                    print('Beagle Caught the Player')
                    print('Beagle is the Winner!!')
                    time.sleep(5)
                    beagle.dispose()
                    break

          self.current_distance = beagle.front_lidar()
          print(self.current_distance)
          msg = Float64()
          msg.data = self.current_distance
          self.publisher.publish(msg)

          feedback_msg.current_distance = self.current_distance
          goal_handle.publish_feedback(feedback_msg)

          time.sleep(0.1)

          return Distbeagle.Result(success=False)
     
     def update_parameter(self, params): # 파라미터(멸망전 모드) 설정 함수
          for param in params:
               if param.name == 'end_game' and param.type_ == Parameter.Type.INTEGER:
                    self.end_game = param.value
                    self.wheel_speed = 15*(self.end_game)
          return SetParametersResult(successful=True)



def main(args = sys.argv[1:]) :
     parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter) # 실행 인자 코드 시작
     parser.add_argument(
          '-g',
          '--set_move_point',
          type=int,
          default=0,
          help='Initial Position Set to:')
     parser.add_argument(
          'argv', nargs=argparse.REMAINDER,
          help='Pass arbitrary arguments to the executable')
     args = parser.parse_args() # 실행 인자 코드 끝

     rp .init(args = args.argv)
     direct_mode_subscribe = direct_mode_sub()

     executor = MultiThreadedExecutor(num_threads=2) # 콜백 함수 병렬 처리용 

     executor.add_node(direct_mode_subscribe) # 콜백 함수 병렬 처리용

    
     try:
          direct_mode_subscribe.save_move_point(args.set_move_point) # 실행 인자
          try:
               executor.spin()
                    
          except KeyboardInterrupt:
               direct_mode_subscribe.get_logger().info('Keyboard Interrupt (SIGINT)')
          finally:
               executor.shutdown()
               direct_mode_subscribe.destroy_node()
     finally:
          rp.shutdown()

if __name__== '__main__' :

     main()