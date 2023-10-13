#tools=['Jenkins', 'Docker', 'K8s', 'Terraform', 90]
#print(tools)
#print(tools[0])
#print(tools[1])
#print(tools[1:4])
#print(tools[1:4][1])


devops={"skill": "DevOps", "Year":2023, "Tech":{"Cloud":"Aws", "Containers":"K8s", "CICD":"Jenkins",} }
print(devops)

#JSON format example:

devops={
        "skill": "DevOps",
        "Year":2023,
        "Tech":
            {
                "Cloud":"Aws",
                "Containers":"K8s",
                "CICD":"Jenkins",
                "GitOps":
                    [
                        "GitOps",
                        "ArgoCD",
                        "Tekton"
                    ]
            }
    }
print(devops)