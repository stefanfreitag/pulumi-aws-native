// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EMRContainers.Inputs
{

    public sealed class VirtualClusterContainerProviderArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the container cluster
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        [Input("info", required: true)]
        public Input<Inputs.VirtualClusterContainerInfoArgs> Info { get; set; } = null!;

        /// <summary>
        /// The type of the container provider
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public VirtualClusterContainerProviderArgs()
        {
        }
    }
}
