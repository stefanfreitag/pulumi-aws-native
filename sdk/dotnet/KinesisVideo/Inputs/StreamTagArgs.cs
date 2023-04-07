// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisVideo.Inputs
{

    /// <summary>
    /// A key-value pair to associated with the Kinesis Video Stream.
    /// </summary>
    public sealed class StreamTagArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The key name of the tag. Specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. The following characters can be used: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        /// </summary>
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        /// <summary>
        /// The value for the tag. Specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. The following characters can be used: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        /// </summary>
        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public StreamTagArgs()
        {
        }
        public static new StreamTagArgs Empty => new StreamTagArgs();
    }
}
