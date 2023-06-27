// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2.Inputs
{

    /// <summary>
    /// Specifies the tags to apply to a resource when the resource is created for the launch template.
    /// </summary>
    public sealed class LaunchTemplateTagSpecificationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The type of resource to tag.
        /// </summary>
        [Input("resourceType")]
        public Input<string>? ResourceType { get; set; }

        [Input("tags")]
        private InputList<Inputs.LaunchTemplateTagArgs>? _tags;

        /// <summary>
        /// The tags for the resource.
        /// </summary>
        public InputList<Inputs.LaunchTemplateTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.LaunchTemplateTagArgs>());
            set => _tags = value;
        }

        public LaunchTemplateTagSpecificationArgs()
        {
        }
        public static new LaunchTemplateTagSpecificationArgs Empty => new LaunchTemplateTagSpecificationArgs();
    }
}
