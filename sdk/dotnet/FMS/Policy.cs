// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.FMS
{
    /// <summary>
    /// Creates an AWS Firewall Manager policy.
    /// </summary>
    [AwsNativeResourceType("aws-native:fms:Policy")]
    public partial class Policy : Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("deleteAllPolicyResources")]
        public Output<bool?> DeleteAllPolicyResources { get; private set; } = null!;

        [Output("excludeMap")]
        public Output<Outputs.PolicyIEMap?> ExcludeMap { get; private set; } = null!;

        [Output("excludeResourceTags")]
        public Output<bool> ExcludeResourceTags { get; private set; } = null!;

        [Output("includeMap")]
        public Output<Outputs.PolicyIEMap?> IncludeMap { get; private set; } = null!;

        [Output("policyName")]
        public Output<string> PolicyName { get; private set; } = null!;

        [Output("remediationEnabled")]
        public Output<bool> RemediationEnabled { get; private set; } = null!;

        [Output("resourceTags")]
        public Output<ImmutableArray<Outputs.PolicyResourceTag>> ResourceTags { get; private set; } = null!;

        [Output("resourceType")]
        public Output<string> ResourceType { get; private set; } = null!;

        [Output("resourceTypeList")]
        public Output<ImmutableArray<string>> ResourceTypeList { get; private set; } = null!;

        [Output("securityServicePolicyData")]
        public Output<object> SecurityServicePolicyData { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.PolicyPolicyTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Policy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Policy(string name, PolicyArgs args, CustomResourceOptions? options = null)
            : base("aws-native:fms:Policy", name, args ?? new PolicyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Policy(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:fms:Policy", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Policy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Policy Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Policy(name, id, options);
        }
    }

    public sealed class PolicyArgs : Pulumi.ResourceArgs
    {
        [Input("deleteAllPolicyResources")]
        public Input<bool>? DeleteAllPolicyResources { get; set; }

        [Input("excludeMap")]
        public Input<Inputs.PolicyIEMapArgs>? ExcludeMap { get; set; }

        [Input("excludeResourceTags", required: true)]
        public Input<bool> ExcludeResourceTags { get; set; } = null!;

        [Input("includeMap")]
        public Input<Inputs.PolicyIEMapArgs>? IncludeMap { get; set; }

        [Input("policyName", required: true)]
        public Input<string> PolicyName { get; set; } = null!;

        [Input("remediationEnabled", required: true)]
        public Input<bool> RemediationEnabled { get; set; } = null!;

        [Input("resourceTags")]
        private InputList<Inputs.PolicyResourceTagArgs>? _resourceTags;
        public InputList<Inputs.PolicyResourceTagArgs> ResourceTags
        {
            get => _resourceTags ?? (_resourceTags = new InputList<Inputs.PolicyResourceTagArgs>());
            set => _resourceTags = value;
        }

        [Input("resourceType", required: true)]
        public Input<string> ResourceType { get; set; } = null!;

        [Input("resourceTypeList")]
        private InputList<string>? _resourceTypeList;
        public InputList<string> ResourceTypeList
        {
            get => _resourceTypeList ?? (_resourceTypeList = new InputList<string>());
            set => _resourceTypeList = value;
        }

        [Input("securityServicePolicyData", required: true)]
        public Input<object> SecurityServicePolicyData { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.PolicyPolicyTagArgs>? _tags;
        public InputList<Inputs.PolicyPolicyTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.PolicyPolicyTagArgs>());
            set => _tags = value;
        }

        public PolicyArgs()
        {
        }
    }
}
