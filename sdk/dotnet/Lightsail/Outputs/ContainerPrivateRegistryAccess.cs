// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lightsail.Outputs
{

    /// <summary>
    /// An object to describe the configuration for the container service to access private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.
    /// </summary>
    [OutputType]
    public sealed class ContainerPrivateRegistryAccess
    {
        /// <summary>
        /// An object to describe a request to activate or deactivate the role that you can use to grant an Amazon Lightsail container service access to Amazon Elastic Container Registry (Amazon ECR) private repositories.
        /// </summary>
        public readonly Outputs.ContainerPrivateRegistryAccessEcrImagePullerRoleProperties? EcrImagePullerRole;

        [OutputConstructor]
        private ContainerPrivateRegistryAccess(Outputs.ContainerPrivateRegistryAccessEcrImagePullerRoleProperties? ecrImagePullerRole)
        {
            EcrImagePullerRole = ecrImagePullerRole;
        }
    }
}
