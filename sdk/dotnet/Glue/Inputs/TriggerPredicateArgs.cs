// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue.Inputs
{

    public sealed class TriggerPredicateArgs : global::Pulumi.ResourceArgs
    {
        [Input("conditions")]
        private InputList<Inputs.TriggerConditionArgs>? _conditions;
        public InputList<Inputs.TriggerConditionArgs> Conditions
        {
            get => _conditions ?? (_conditions = new InputList<Inputs.TriggerConditionArgs>());
            set => _conditions = value;
        }

        [Input("logical")]
        public Input<string>? Logical { get; set; }

        public TriggerPredicateArgs()
        {
        }
        public static new TriggerPredicateArgs Empty => new TriggerPredicateArgs();
    }
}
