// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Route53RecoveryControl
{
    /// <summary>
    /// Resource schema for AWS Route53 Recovery Control basic constructs and validation rules.
    /// </summary>
    [AwsNativeResourceType("aws-native:route53recoverycontrol:SafetyRule")]
    public partial class SafetyRule : global::Pulumi.CustomResource
    {
        [Output("assertionRule")]
        public Output<Outputs.SafetyRuleAssertionRule?> AssertionRule { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the control panel.
        /// </summary>
        [Output("controlPanelArn")]
        public Output<string?> ControlPanelArn { get; private set; } = null!;

        [Output("gatingRule")]
        public Output<Outputs.SafetyRuleGatingRule?> GatingRule { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("ruleConfig")]
        public Output<Outputs.SafetyRuleRuleConfig?> RuleConfig { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the safety rule.
        /// </summary>
        [Output("safetyRuleArn")]
        public Output<string> SafetyRuleArn { get; private set; } = null!;

        /// <summary>
        /// The deployment status of the routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.
        /// </summary>
        [Output("status")]
        public Output<Pulumi.AwsNative.Route53RecoveryControl.SafetyRuleStatus> Status { get; private set; } = null!;

        /// <summary>
        /// A collection of tags associated with a resource
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.CreateOnlyTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a SafetyRule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SafetyRule(string name, SafetyRuleArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:route53recoverycontrol:SafetyRule", name, args ?? new SafetyRuleArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SafetyRule(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:route53recoverycontrol:SafetyRule", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "controlPanelArn",
                    "ruleConfig",
                    "tags[*]",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing SafetyRule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SafetyRule Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new SafetyRule(name, id, options);
        }
    }

    public sealed class SafetyRuleArgs : global::Pulumi.ResourceArgs
    {
        [Input("assertionRule")]
        public Input<Inputs.SafetyRuleAssertionRuleArgs>? AssertionRule { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the control panel.
        /// </summary>
        [Input("controlPanelArn")]
        public Input<string>? ControlPanelArn { get; set; }

        [Input("gatingRule")]
        public Input<Inputs.SafetyRuleGatingRuleArgs>? GatingRule { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("ruleConfig")]
        public Input<Inputs.SafetyRuleRuleConfigArgs>? RuleConfig { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.CreateOnlyTagArgs>? _tags;

        /// <summary>
        /// A collection of tags associated with a resource
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.CreateOnlyTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.CreateOnlyTagArgs>());
            set => _tags = value;
        }

        public SafetyRuleArgs()
        {
        }
        public static new SafetyRuleArgs Empty => new SafetyRuleArgs();
    }
}
