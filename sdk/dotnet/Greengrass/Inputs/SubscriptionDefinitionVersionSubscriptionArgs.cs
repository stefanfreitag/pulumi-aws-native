// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Greengrass.Inputs
{

    public sealed class SubscriptionDefinitionVersionSubscriptionArgs : global::Pulumi.ResourceArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        [Input("source", required: true)]
        public Input<string> Source { get; set; } = null!;

        [Input("subject", required: true)]
        public Input<string> Subject { get; set; } = null!;

        [Input("target", required: true)]
        public Input<string> Target { get; set; } = null!;

        public SubscriptionDefinitionVersionSubscriptionArgs()
        {
        }
        public static new SubscriptionDefinitionVersionSubscriptionArgs Empty => new SubscriptionDefinitionVersionSubscriptionArgs();
    }
}
