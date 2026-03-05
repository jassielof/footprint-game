variable "DOCKERFILES" {
    default = fileset("docker", "*.Dockerfile")
}

group "default" {
    targets = [for f in DOCKERFILES : replace(basename(f), ".Dockerfile", "")]
}

target "default" {
    context = "."
}

target "*" {
    dockerfile = "docker/${target.name}.Dockerfile"
}
