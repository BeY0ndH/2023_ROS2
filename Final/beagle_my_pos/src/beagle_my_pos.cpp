#include <memory>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <stdexcept>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using std::placeholders::_1;



class beagle_my_pos : public rclcpp::Node
{
  

  public:
    static int my_pos;
    beagle_my_pos()
    : Node("beagle_my_pos")
    {
      subscription_ = this->create_subscription<std_msgs::msg::String>(
      "topic", 10, std::bind(&beagle_my_pos::topic_callback, this, _1));
    }

  private:
    void topic_callback(const std_msgs::msg::String::SharedPtr msg) const
    {
      std::string data = msg->data;

      

      if (data == "DICE0")
      {
        my_pos = my_pos + 0;
        if (this->my_pos >= 16)
        {
          this->my_pos -= 16;
        }
        RCLCPP_INFO(this->get_logger(), "I'm at tile #'%d'", this->my_pos);
      }

      else if (data == "DICE1")
      {
        this->my_pos += 1;
        if (this->my_pos >= 16)
        {
          this->my_pos -= 16;
        }
        RCLCPP_INFO(this->get_logger(), "I'm at tile #'%d'", this->my_pos);
      }

      else if (data == "DICE2")
      {
        this->my_pos += 2;
        if (this->my_pos >= 16)
        {
          this->my_pos -= 16;
        }
        RCLCPP_INFO(this->get_logger(), "I'm at tile #'%d'", this->my_pos);
      }

      else if (data == "DICE3")
      {
        this->my_pos += 3;
        if (this->my_pos >= 16)
        {
          this->my_pos -= 16;
        }
        RCLCPP_INFO(this->get_logger(), "I'm at tile #'%d'", this->my_pos);
      }

      else if (data == "DICE4")
      {
        this->my_pos += 4;
        if (this->my_pos >= 16)
        {
          this->my_pos -= 16;
        }
        RCLCPP_INFO(this->get_logger(), "I'm at tile #'%d'", this->my_pos);
      }

      else if (data == "DICE5")
      {
        this->my_pos += 5;
        if (this->my_pos >= 16)
        {
          this->my_pos -= 16;
        }
        RCLCPP_INFO(this->get_logger(), "I'm at tile #'%d'", this->my_pos);
      }

      else if (data == "DICE6")
      {
        this->my_pos += 6;
        if (this->my_pos >= 16)
        {
          this->my_pos -= 16;
        }
        RCLCPP_INFO(this->get_logger(), "I'm at tile #'%d'", this->my_pos);
      }

     
    }
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

int beagle_my_pos::my_pos = 0;

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<beagle_my_pos>());
  rclcpp::shutdown();
  return 0;
}