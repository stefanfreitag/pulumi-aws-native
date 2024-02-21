// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodePipeline.Inputs
{

    public sealed class PipelineGitPullRequestFilterArgs : global::Pulumi.ResourceArgs
    {
        [Input("branches")]
        public Input<Inputs.PipelineGitBranchFilterCriteriaArgs>? Branches { get; set; }

        [Input("events")]
        private InputList<string>? _events;
        public InputList<string> Events
        {
            get => _events ?? (_events = new InputList<string>());
            set => _events = value;
        }

        [Input("filePaths")]
        public Input<Inputs.PipelineGitFilePathFilterCriteriaArgs>? FilePaths { get; set; }

        public PipelineGitPullRequestFilterArgs()
        {
        }
        public static new PipelineGitPullRequestFilterArgs Empty => new PipelineGitPullRequestFilterArgs();
    }
}
