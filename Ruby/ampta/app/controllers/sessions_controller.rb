class SessionsController < ApplicationController

	before_filter :authenticate_user, :only => [:home, :profile, :setting]

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
						
						render "login"	
					end
				end

  def home
  end

  def profile
  end

  def setting
  end

  def logout
	session[:user_id] = nil
	redirect_to :action => 'login'
  end
end
