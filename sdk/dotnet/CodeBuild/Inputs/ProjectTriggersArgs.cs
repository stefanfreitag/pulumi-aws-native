// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodeBuild.Inputs
{

    public sealed class ProjectTriggersArgs : global::Pulumi.ResourceArgs
    {
        [Input("buildType")]
        public Input<string>? BuildType { get; set; }

        [Input("filterGroups")]
        private InputList<Inputs.ProjectFilterGroupArgs>? _filterGroups;
        public InputList<Inputs.ProjectFilterGroupArgs> FilterGroups
        {
            get => _filterGroups ?? (_filterGroups = new InputList<Inputs.ProjectFilterGroupArgs>());
            set => _filterGroups = value;
        }

        [Input("webhook")]
        public Input<bool>? Webhook { get; set; }

        public ProjectTriggersArgs()
        {
        }
        public static new ProjectTriggersArgs Empty => new ProjectTriggersArgs();
    }
}
