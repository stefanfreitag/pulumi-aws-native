// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WaFv2
{
    /// <summary>
    /// Contains the Rules that identify the requests that you want to allow, block, or count. In a WebACL, you also specify a default action (ALLOW or BLOCK), and the action for each Rule that you add to a WebACL, for example, block requests from specified IP addresses or block requests from specified referrers. You also associate the WebACL with a CloudFront distribution to identify the requests that you want AWS WAF to filter. If you add more than one Rule to a WebACL, a request needs to match only one of the specifications to be allowed, blocked, or counted.
    /// </summary>
    [AwsNativeResourceType("aws-native:wafv2:WebAcl")]
    public partial class WebAcl : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("associationConfig")]
        public Output<Outputs.WebAclAssociationConfig?> AssociationConfig { get; private set; } = null!;

        [Output("capacity")]
        public Output<int> Capacity { get; private set; } = null!;

        [Output("captchaConfig")]
        public Output<Outputs.WebAclCaptchaConfig?> CaptchaConfig { get; private set; } = null!;

        [Output("challengeConfig")]
        public Output<Outputs.WebAclChallengeConfig?> ChallengeConfig { get; private set; } = null!;

        [Output("customResponseBodies")]
        public Output<ImmutableDictionary<string, Outputs.WebAclCustomResponseBody>?> CustomResponseBodies { get; private set; } = null!;

        [Output("defaultAction")]
        public Output<Outputs.WebAclDefaultAction> DefaultAction { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("labelNamespace")]
        public Output<string> LabelNamespace { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// Collection of Rules.
        /// </summary>
        [Output("rules")]
        public Output<ImmutableArray<Outputs.WebAclRule>> Rules { get; private set; } = null!;

        [Output("scope")]
        public Output<Pulumi.AwsNative.WaFv2.WebAclScope> Scope { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        [Output("tokenDomains")]
        public Output<ImmutableArray<string>> TokenDomains { get; private set; } = null!;

        [Output("visibilityConfig")]
        public Output<Outputs.WebAclVisibilityConfig> VisibilityConfig { get; private set; } = null!;


        /// <summary>
        /// Create a WebAcl resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public WebAcl(string name, WebAclArgs args, CustomResourceOptions? options = null)
            : base("aws-native:wafv2:WebAcl", name, args ?? new WebAclArgs(), MakeResourceOptions(options, ""))
        {
        }

        private WebAcl(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:wafv2:WebAcl", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "name",
                    "scope",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing WebAcl resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static WebAcl Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new WebAcl(name, id, options);
        }
    }

    public sealed class WebAclArgs : global::Pulumi.ResourceArgs
    {
        [Input("associationConfig")]
        public Input<Inputs.WebAclAssociationConfigArgs>? AssociationConfig { get; set; }

        [Input("captchaConfig")]
        public Input<Inputs.WebAclCaptchaConfigArgs>? CaptchaConfig { get; set; }

        [Input("challengeConfig")]
        public Input<Inputs.WebAclChallengeConfigArgs>? ChallengeConfig { get; set; }

        [Input("customResponseBodies")]
        private InputMap<Inputs.WebAclCustomResponseBodyArgs>? _customResponseBodies;
        public InputMap<Inputs.WebAclCustomResponseBodyArgs> CustomResponseBodies
        {
            get => _customResponseBodies ?? (_customResponseBodies = new InputMap<Inputs.WebAclCustomResponseBodyArgs>());
            set => _customResponseBodies = value;
        }

        [Input("defaultAction", required: true)]
        public Input<Inputs.WebAclDefaultActionArgs> DefaultAction { get; set; } = null!;

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("rules")]
        private InputList<Inputs.WebAclRuleArgs>? _rules;

        /// <summary>
        /// Collection of Rules.
        /// </summary>
        public InputList<Inputs.WebAclRuleArgs> Rules
        {
            get => _rules ?? (_rules = new InputList<Inputs.WebAclRuleArgs>());
            set => _rules = value;
        }

        [Input("scope", required: true)]
        public Input<Pulumi.AwsNative.WaFv2.WebAclScope> Scope { get; set; } = null!;

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        [Input("tokenDomains")]
        private InputList<string>? _tokenDomains;
        public InputList<string> TokenDomains
        {
            get => _tokenDomains ?? (_tokenDomains = new InputList<string>());
            set => _tokenDomains = value;
        }

        [Input("visibilityConfig", required: true)]
        public Input<Inputs.WebAclVisibilityConfigArgs> VisibilityConfig { get; set; } = null!;

        public WebAclArgs()
        {
        }
        public static new WebAclArgs Empty => new WebAclArgs();
    }
}
