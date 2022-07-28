// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2.Inputs
{

    public sealed class NetworkInsightsAccessScopeAccessScopePathRequestArgs : global::Pulumi.ResourceArgs
    {
        [Input("destination")]
        public Input<Inputs.NetworkInsightsAccessScopePathStatementRequestArgs>? Destination { get; set; }

        [Input("source")]
        public Input<Inputs.NetworkInsightsAccessScopePathStatementRequestArgs>? Source { get; set; }

        [Input("throughResources")]
        private InputList<Inputs.NetworkInsightsAccessScopeThroughResourcesStatementRequestArgs>? _throughResources;
        public InputList<Inputs.NetworkInsightsAccessScopeThroughResourcesStatementRequestArgs> ThroughResources
        {
            get => _throughResources ?? (_throughResources = new InputList<Inputs.NetworkInsightsAccessScopeThroughResourcesStatementRequestArgs>());
            set => _throughResources = value;
        }

        public NetworkInsightsAccessScopeAccessScopePathRequestArgs()
        {
        }
        public static new NetworkInsightsAccessScopeAccessScopePathRequestArgs Empty => new NetworkInsightsAccessScopeAccessScopePathRequestArgs();
    }
}
