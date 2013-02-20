class UsersController < ApplicationController

before_filter :authenticate_user, :home

	def show
		@user = User.find(params[:id])
	end
	
	
end
