// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Greengrass.Inputs
{

    public sealed class ResourceDefinitionResourceInstanceArgs : global::Pulumi.ResourceArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("resourceDataContainer", required: true)]
        public Input<Inputs.ResourceDefinitionResourceDataContainerArgs> ResourceDataContainer { get; set; } = null!;

        public ResourceDefinitionResourceInstanceArgs()
        {
        }
        public static new ResourceDefinitionResourceInstanceArgs Empty => new ResourceDefinitionResourceInstanceArgs();
    }
}
