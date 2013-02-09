class UsersController < ApplicationController

before_filter :save_login_state, :only => [:new, :create]

	def show
		@user = User.find(params[:id])
	end
	
	def new
		
	end	

	


end
