// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodeDeploy.Inputs
{

    public sealed class DeploymentGroupOnPremisesTagSetArgs : global::Pulumi.ResourceArgs
    {
        [Input("onPremisesTagSetList")]
        private InputList<Inputs.DeploymentGroupOnPremisesTagSetListObjectArgs>? _onPremisesTagSetList;
        public InputList<Inputs.DeploymentGroupOnPremisesTagSetListObjectArgs> OnPremisesTagSetList
        {
            get => _onPremisesTagSetList ?? (_onPremisesTagSetList = new InputList<Inputs.DeploymentGroupOnPremisesTagSetListObjectArgs>());
            set => _onPremisesTagSetList = value;
        }

        public DeploymentGroupOnPremisesTagSetArgs()
        {
        }
        public static new DeploymentGroupOnPremisesTagSetArgs Empty => new DeploymentGroupOnPremisesTagSetArgs();
    }
}
