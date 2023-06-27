// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue.Inputs
{

    public sealed class TriggerEventBatchingConditionArgs : global::Pulumi.ResourceArgs
    {
        [Input("batchSize", required: true)]
        public Input<int> BatchSize { get; set; } = null!;

        [Input("batchWindow")]
        public Input<int>? BatchWindow { get; set; }

        public TriggerEventBatchingConditionArgs()
        {
        }
        public static new TriggerEventBatchingConditionArgs Empty => new TriggerEventBatchingConditionArgs();
    }
}
