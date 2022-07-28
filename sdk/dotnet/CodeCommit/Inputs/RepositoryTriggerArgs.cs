// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodeCommit.Inputs
{

    public sealed class RepositoryTriggerArgs : global::Pulumi.ResourceArgs
    {
        [Input("branches")]
        private InputList<string>? _branches;
        public InputList<string> Branches
        {
            get => _branches ?? (_branches = new InputList<string>());
            set => _branches = value;
        }

        [Input("customData")]
        public Input<string>? CustomData { get; set; }

        [Input("destinationArn", required: true)]
        public Input<string> DestinationArn { get; set; } = null!;

        [Input("events", required: true)]
        private InputList<string>? _events;
        public InputList<string> Events
        {
            get => _events ?? (_events = new InputList<string>());
            set => _events = value;
        }

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public RepositoryTriggerArgs()
        {
        }
        public static new RepositoryTriggerArgs Empty => new RepositoryTriggerArgs();
    }
}
