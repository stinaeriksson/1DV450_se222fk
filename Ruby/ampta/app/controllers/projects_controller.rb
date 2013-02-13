# encoding: utf-8
class ProjectsController < ApplicationController
	before_filter :authenticate_user, :only => [:create, :edit]

	def index
		@projects = Project.all
	end
	
	def show
		@project = Project.find(params[:id])
		@users_in_project = @project.users
		@tickets_for_project =@project.tickets
	end

	def destroy
		@project = Project.find(params[:id])
		@project.destroy
		redirect_to :root	
	end

	def new
		@project = Project.new
		
	end


	def create
		@id = @current_user.id
		@user = User.where(["id = ?", @id]) 
		@project = Project.new(params[:project])
		@project.users << @user

		if @project.save
			flash[:notice] = "Projekt sparat"
			redirect_to :action => "show", :id => @project.id
		else
			render :action => "new"
		end
	end

	def edit
		@id = @current_user.id
		@project = Project.find(params[:id])
		@pid = @project.owner_id
		

		unless @id == @pid
			
			flash[:notice] = "Du har ej rättigheter att redigera projektet"
			redirect_to :action => "show", :id => @project.id
			
		end

	end

	def update
		@project = Project.find(params[:id])
		if @project.update_attributes(params[:project])
			flash[:notice] = "Projektet uppdaterat!"
			redirect_to project_path
		else
			render :action => "edit"
		end
	end


end
