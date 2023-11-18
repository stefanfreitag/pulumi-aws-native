// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ImageBuilder.Inputs
{

    /// <summary>
    /// The included resources of the policy detail.
    /// </summary>
    public sealed class LifecyclePolicyIncludeResourcesArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Use to configure lifecycle actions on AMIs.
        /// </summary>
        [Input("amis")]
        public Input<bool>? Amis { get; set; }

        /// <summary>
        /// Use to configure lifecycle actions on containers.
        /// </summary>
        [Input("containers")]
        public Input<bool>? Containers { get; set; }

        /// <summary>
        /// Use to configure lifecycle actions on snapshots.
        /// </summary>
        [Input("snapshots")]
        public Input<bool>? Snapshots { get; set; }

        public LifecyclePolicyIncludeResourcesArgs()
        {
        }
        public static new LifecyclePolicyIncludeResourcesArgs Empty => new LifecyclePolicyIncludeResourcesArgs();
    }
}
