# -*- mode: ruby -*-
# vi: set ft=ruby :
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Beginning of vm "rpmbuild" configuration section
  config.vm.define "rpmbuild" do |server|
    server.vm.box = "centos64"
    server.vm.box_url = "https://github.com/2creatives/vagrant-centos/releases/download/v6.4.2/centos64-x86_64-20140116.box"
    server.vm.network :private_network, ip: "10.10.0.11"
    server.vm.hostname = "rpmbuild.charlymps.com"
    server.vm.provision :ansible do |ansible|
      ansible.playbook = "ansible/rpmbuild.yml"
      # This is required because to prevent Host key checking errors when the vagrant machine is recreated with another key
      ansible.host_key_checking = false
    end
  end

end
