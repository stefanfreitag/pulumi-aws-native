// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ResourceGroups.Inputs
{

    public sealed class GroupConfigurationItemArgs : Pulumi.ResourceArgs
    {
        [Input("parameters")]
        private InputList<Inputs.GroupConfigurationParameterArgs>? _parameters;
        public InputList<Inputs.GroupConfigurationParameterArgs> Parameters
        {
            get => _parameters ?? (_parameters = new InputList<Inputs.GroupConfigurationParameterArgs>());
            set => _parameters = value;
        }

        [Input("type")]
        public Input<string>? Type { get; set; }

        public GroupConfigurationItemArgs()
        {
        }
    }
}
