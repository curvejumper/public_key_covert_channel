# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
    # The most common configuration options are documented and commented below.
    # For a complete reference, please see the online documentation at
    # https://docs.vagrantup.com.
    # Every Vagrant development environment requires a box. You can search for
    # boxes at https://vagrantcloud.com/search.
    config.vm.define "router" do |router|
        router.vm.box = "ubuntu/focal64"
        router.vm.network :private_network, ip: "192.168.50.1", netmask:"255.255.255.0"
        router.vm.network :public_network, bridge: "en0: Wi-Fi (AirPort)"
        router.vm.provider :VirtualBox do |vb|
              vb.customize ["modifyvm", :id, "--nicpromisc1", "allow-all","--nicpromisc2", "allow-all"]
              end
        router.vm.provision "shell",
            run: "always",
            inline: <<-SHELL
            sysctl net.ipv4.ip_forward=1
            route add default gw 192.168.2.1 2>/dev/null || true
           SHELL
    end
    config.vm.define "server" do |server|
        server.vm.box = "ubuntu/focal64"
        server.vm.network :private_network, ip: "192.168.50.2",netmask:"255.255.255.0"
        server.vm.provision "shell",
            run: "always",
            inline: <<-SHELL
            route add default gw 192.168.50.1 2>/dev/null || true
            SHELL
    end
    config.vm.define "client" do |client|
        client.vm.box = "ubuntu/focal64"
        client.vm.network :private_network, ip: "192.168.50.3",netmask:"255.255.255.0"
        client.vm.provision "shell",
             run: "always",
             inline: <<-SHELL
              route add default gw 192.168.50.1 2>/dev/null || true
              echo "192.168.50.2      server.com" >> /etc/hosts
             SHELL
    end
  
    config.vm.synced_folder "./", "/home/vagrant/code"
  
    config.vm.provider "virtualbox" do |vb|
      # Display the VirtualBox GUI when booting the machine
      vb.gui = false
  
      # Customize the amount of memory on the VM:
      vb.memory = "1024"
    end
    #
    # View the documentation for the provider you are using for more
    # information on available options.
  
    # Enable provisioning with a shell script. Additional provisioners such as
    # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
    # documentation for more information about their specific syntax and use.
  
    config.vm.provision "shell", run: "always",inline: <<-SHELL
      sudo apt-get update -y
      sudo apt upgrade -y
      sudo apt install -y openssl build-essential libssl-dev libffi-dev
      sudo apt install -y python3-pip rustc openssl build-essential libssl-dev libffi-dev python3-dev python3
    SHELL
  
  end
  