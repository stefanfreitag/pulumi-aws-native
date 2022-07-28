// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SSM
{
    public static class GetPatchBaseline
    {
        /// <summary>
        /// Resource Type definition for AWS::SSM::PatchBaseline
        /// </summary>
        public static Task<GetPatchBaselineResult> InvokeAsync(GetPatchBaselineArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPatchBaselineResult>("aws-native:ssm:getPatchBaseline", args ?? new GetPatchBaselineArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::SSM::PatchBaseline
        /// </summary>
        public static Output<GetPatchBaselineResult> Invoke(GetPatchBaselineInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetPatchBaselineResult>("aws-native:ssm:getPatchBaseline", args ?? new GetPatchBaselineInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPatchBaselineArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetPatchBaselineArgs()
        {
        }
        public static new GetPatchBaselineArgs Empty => new GetPatchBaselineArgs();
    }

    public sealed class GetPatchBaselineInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetPatchBaselineInvokeArgs()
        {
        }
        public static new GetPatchBaselineInvokeArgs Empty => new GetPatchBaselineInvokeArgs();
    }


    [OutputType]
    public sealed class GetPatchBaselineResult
    {
        public readonly Outputs.PatchBaselineRuleGroup? ApprovalRules;
        public readonly ImmutableArray<string> ApprovedPatches;
        public readonly string? ApprovedPatchesComplianceLevel;
        public readonly bool? ApprovedPatchesEnableNonSecurity;
        public readonly string? Description;
        public readonly Outputs.PatchBaselinePatchFilterGroup? GlobalFilters;
        public readonly string? Id;
        public readonly string? Name;
        public readonly ImmutableArray<string> PatchGroups;
        public readonly ImmutableArray<string> RejectedPatches;
        public readonly string? RejectedPatchesAction;
        public readonly ImmutableArray<Outputs.PatchBaselinePatchSource> Sources;
        public readonly ImmutableArray<Outputs.PatchBaselineTag> Tags;

        [OutputConstructor]
        private GetPatchBaselineResult(
            Outputs.PatchBaselineRuleGroup? approvalRules,

            ImmutableArray<string> approvedPatches,

            string? approvedPatchesComplianceLevel,

            bool? approvedPatchesEnableNonSecurity,

            string? description,

            Outputs.PatchBaselinePatchFilterGroup? globalFilters,

            string? id,

            string? name,

            ImmutableArray<string> patchGroups,

            ImmutableArray<string> rejectedPatches,

            string? rejectedPatchesAction,

            ImmutableArray<Outputs.PatchBaselinePatchSource> sources,

            ImmutableArray<Outputs.PatchBaselineTag> tags)
        {
            ApprovalRules = approvalRules;
            ApprovedPatches = approvedPatches;
            ApprovedPatchesComplianceLevel = approvedPatchesComplianceLevel;
            ApprovedPatchesEnableNonSecurity = approvedPatchesEnableNonSecurity;
            Description = description;
            GlobalFilters = globalFilters;
            Id = id;
            Name = name;
            PatchGroups = patchGroups;
            RejectedPatches = rejectedPatches;
            RejectedPatchesAction = rejectedPatchesAction;
            Sources = sources;
            Tags = tags;
        }
    }
}
