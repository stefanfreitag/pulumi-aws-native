// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pipes.Inputs
{

    public sealed class PipeTargetSqsQueueParametersArgs : global::Pulumi.ResourceArgs
    {
        [Input("messageDeduplicationId")]
        public Input<string>? MessageDeduplicationId { get; set; }

        [Input("messageGroupId")]
        public Input<string>? MessageGroupId { get; set; }

        public PipeTargetSqsQueueParametersArgs()
        {
        }
        public static new PipeTargetSqsQueueParametersArgs Empty => new PipeTargetSqsQueueParametersArgs();
    }
}
