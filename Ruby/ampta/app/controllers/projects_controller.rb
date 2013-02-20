# encoding: utf-8
class ProjectsController < ApplicationController
	before_filter :authenticate_user, :home
	before_filter :control_user, :only => [:show]

	def index
		@all_projects = Project.all

	end
	
	def show

		@project = Project.find(params[:id])
		@users_in_project = @project.users
		@tickets_for_project =@project.tickets
	end

	def destroy
		@id = @current_user.id
		@project = Project.find(params[:id])
		@pid = @project.owner_id
		

		if @id == @pid
			@project = Project.find(params[:id])
			@project.destroy
			redirect_to :root
		else
			flash[:error] = "Du har ej rättigheter att ta bort projektet"
			redirect_to :action => "show", :id => @project.id
		end

		
	end

	def new
		@project = Project.new
		@users = User.all
	end


	def create
		@users = User.all

		@project = Project.new(params[:project])

		if @project.save
			flash[:notice] = "Projekt sparat"
			redirect_to :action => "show", :id => @project.id
		else
			render :action => "new"
		end
	end

	def edit
		@users = User.all
		@id = @current_user.id
		@project = Project.find(params[:id])
		@pid = @project.owner_id
		

		unless @id == @pid
			
			flash[:error] = "Du har ej rättigheter att redigera projektet"
			redirect_to :action => "show", :id => @project.id
			
		end

	end

	def update
		params[:project][:user_ids] ||= []
		@users = User.all
		@project = Project.find(params[:id])
 		
		
		if @project.update_attributes(params[:project])
			flash[:notice] = "Projektet uppdaterat!"
			redirect_to project_path
		else
			render :action => "edit"
		end
	end

	def sort
		@project = Project.all
	end

	def logout
	 session[:user_id] = nil
	 redirect_to :action => 'login', :controller => 'sessions'
    end


end
