# Note: You can use any Debian/Ubuntu based image you want.
FROM mcr.microsoft.com/vscode/devcontainers/python:3.7-bullseye

# [Option] Install zsh
ARG INSTALL_ZSH="true"
# [Option] Upgrade OS packages to their latest versions
ARG UPGRADE_PACKAGES="false"
# [Option] Enable non-root Docker access in container
ARG ENABLE_NONROOT_DOCKER="true"
# [Option] Use the OSS Moby CLI instead of the licensed Docker CLI
ARG USE_MOBY="true"

# Enable new "BUILDKIT" mode for Docker CLI
ENV DOCKER_BUILDKIT=1

# Install needed packages and setup non-root user. Use a separate RUN statement to add your
# own dependencies. A user of "automatic" attempts to reuse an user ID if one already exists.
ARG USERNAME=automatic
ARG USER_UID=1000
ARG USER_GID=$USER_UID
COPY _library-scripts/*.sh /tmp/library-scripts/
RUN apt-get update \
	&& /bin/bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" "true" "true" \
	# Use Docker script from script library to set things up
	&& /bin/bash /tmp/library-scripts/docker-debian.sh "${ENABLE_NONROOT_DOCKER}" "/var/run/docker-host.sock" "/var/run/docker.sock" "${USERNAME}" \
	# Clean up
	&& apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts/

# zsh
RUN zsh
ENV SHELL /usr/bin/zsh

# install libmariadb-dev (for install MariaDB Connector/Python)
RUN sudo apt update
RUN sudo apt install -y libmariadb-dev

ENV PYTHONUNBUFFERED=1
EXPOSE 80

# Setting the ENTRYPOINT to docker-init.sh will configure non-root access
# to the Docker socket. The script will also execute CMD as needed.
ENTRYPOINT [ "/usr/local/share/docker-init.sh" ]
CMD [ "sleep", "infinity" ]

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>


# # wkhtmltopdf をインストールする。
RUN apt install wkhtmltopdf

# 日本語フォントとして Noto Fonts をインストールする。
RUN wget https://noto-website.storage.googleapis.com/pkgs/Noto-unhinted.zip \
 && unzip -d NotoSansJapanese Noto-unhinted.zip \
 && mkdir -p /usr/share/fonts/opentype \
 && mv -fv ./NotoSansJapanese /usr/share/fonts/opentype/NotoSansJapanese \
 && rm -rfv Noto-unhinted.zip \
 && fc-cache -fv
