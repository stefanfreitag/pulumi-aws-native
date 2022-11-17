// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EKS.Inputs
{

    /// <summary>
    /// An object representing the Outpost configuration to use for AWS EKS outpost cluster.
    /// </summary>
    public sealed class ClusterOutpostConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specify the Instance type of the machines that should be used to create your cluster.
        /// </summary>
        [Input("controlPlaneInstanceType", required: true)]
        public Input<string> ControlPlaneInstanceType { get; set; } = null!;

        /// <summary>
        /// Specify the placement group of the control plane machines for your cluster.
        /// </summary>
        [Input("controlPlanePlacement")]
        public Input<Inputs.ClusterControlPlanePlacementArgs>? ControlPlanePlacement { get; set; }

        [Input("outpostArns", required: true)]
        private InputList<string>? _outpostArns;

        /// <summary>
        /// Specify one or more Arn(s) of Outpost(s) on which you would like to create your cluster.
        /// </summary>
        public InputList<string> OutpostArns
        {
            get => _outpostArns ?? (_outpostArns = new InputList<string>());
            set => _outpostArns = value;
        }

        public ClusterOutpostConfigArgs()
        {
        }
        public static new ClusterOutpostConfigArgs Empty => new ClusterOutpostConfigArgs();
    }
}
