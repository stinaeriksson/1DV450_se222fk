class SessionsController < ApplicationController

	before_filter :authenticate_user, :only => [:home]

	before_filter :save_login_state, :only => [:login, :login_attempt]

  def login
  	#Login Form
  end

  def login_attempt
					authorized_user = User.authenticate(params[:email],params[:password])
					if authorized_user
						session[:user_id] = authorized_user.id
						redirect_to(:action => 'home')
					else
						
						redirect_to :root	
					end
				end

  def home
  	@id = @current_user.id
  	
	@projects_for_user = User.find(@id).projects

	@tickets_for_user = User.find(@id).tickets
		
  end

 

  def logout
	session[:user_id] = nil
	redirect_to :action => 'login'
  end
end
