class User < ActiveRecord::Base

  has_secure_password

  attr_accessible :first_name, :last_name, :email, :password
  has_many :tickets
  has_and_belongs_to_many :projects

  def self.authenticate(login_email = "" , login_password = "" )
    user = User.where('email = ?', login_email).first
    if user.try(:authenticate, login_password)
      return user
    else
      return false
    end
  end   

end
