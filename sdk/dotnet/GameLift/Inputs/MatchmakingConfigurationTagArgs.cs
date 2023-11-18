// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GameLift.Inputs
{

    /// <summary>
    /// A key-value pair to associate with a resource.
    /// </summary>
    public sealed class MatchmakingConfigurationTagArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length.
        /// </summary>
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        /// <summary>
        /// The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length.
        /// </summary>
        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public MatchmakingConfigurationTagArgs()
        {
        }
        public static new MatchmakingConfigurationTagArgs Empty => new MatchmakingConfigurationTagArgs();
    }
}
