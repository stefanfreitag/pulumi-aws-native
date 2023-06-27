// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Greengrass.Outputs
{

    [OutputType]
    public sealed class ResourceDefinitionVersionResourceInstance
    {
        public readonly string Id;
        public readonly string Name;
        public readonly Outputs.ResourceDefinitionVersionResourceDataContainer ResourceDataContainer;

        [OutputConstructor]
        private ResourceDefinitionVersionResourceInstance(
            string id,

            string name,

            Outputs.ResourceDefinitionVersionResourceDataContainer resourceDataContainer)
        {
            Id = id;
            Name = name;
            ResourceDataContainer = resourceDataContainer;
        }
    }
}
