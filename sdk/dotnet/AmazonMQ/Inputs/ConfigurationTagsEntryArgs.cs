// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AmazonMQ.Inputs
{

    public sealed class ConfigurationTagsEntryArgs : global::Pulumi.ResourceArgs
    {
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public ConfigurationTagsEntryArgs()
        {
        }
        public static new ConfigurationTagsEntryArgs Empty => new ConfigurationTagsEntryArgs();
    }
}
