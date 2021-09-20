// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SSMIncidents
{
    /// <summary>
    /// Resource type definition for AWS::SSMIncidents::ResponsePlan
    /// </summary>
    [AwsNativeResourceType("aws-native:ssmincidents:ResponsePlan")]
    public partial class ResponsePlan : Pulumi.CustomResource
    {
        /// <summary>
        /// The list of actions.
        /// </summary>
        [Output("actions")]
        public Output<ImmutableArray<Outputs.ResponsePlanAction>> Actions { get; private set; } = null!;

        /// <summary>
        /// The ARN of the response plan.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("chatChannel")]
        public Output<Outputs.ResponsePlanChatChannel?> ChatChannel { get; private set; } = null!;

        /// <summary>
        /// The display name of the response plan.
        /// </summary>
        [Output("displayName")]
        public Output<string?> DisplayName { get; private set; } = null!;

        /// <summary>
        /// The list of engagements to use.
        /// </summary>
        [Output("engagements")]
        public Output<ImmutableArray<string>> Engagements { get; private set; } = null!;

        [Output("incidentTemplate")]
        public Output<Outputs.ResponsePlanIncidentTemplate> IncidentTemplate { get; private set; } = null!;

        /// <summary>
        /// The name of the response plan.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The tags to apply to the response plan.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ResponsePlanTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ResponsePlan resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ResponsePlan(string name, ResponsePlanArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ssmincidents:ResponsePlan", name, args ?? new ResponsePlanArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ResponsePlan(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ssmincidents:ResponsePlan", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ResponsePlan resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ResponsePlan Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ResponsePlan(name, id, options);
        }
    }

    public sealed class ResponsePlanArgs : Pulumi.ResourceArgs
    {
        [Input("actions")]
        private InputList<Inputs.ResponsePlanActionArgs>? _actions;

        /// <summary>
        /// The list of actions.
        /// </summary>
        public InputList<Inputs.ResponsePlanActionArgs> Actions
        {
            get => _actions ?? (_actions = new InputList<Inputs.ResponsePlanActionArgs>());
            set => _actions = value;
        }

        [Input("chatChannel")]
        public Input<Inputs.ResponsePlanChatChannelArgs>? ChatChannel { get; set; }

        /// <summary>
        /// The display name of the response plan.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        [Input("engagements")]
        private InputList<string>? _engagements;

        /// <summary>
        /// The list of engagements to use.
        /// </summary>
        public InputList<string> Engagements
        {
            get => _engagements ?? (_engagements = new InputList<string>());
            set => _engagements = value;
        }

        [Input("incidentTemplate", required: true)]
        public Input<Inputs.ResponsePlanIncidentTemplateArgs> IncidentTemplate { get; set; } = null!;

        /// <summary>
        /// The name of the response plan.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.ResponsePlanTagArgs>? _tags;

        /// <summary>
        /// The tags to apply to the response plan.
        /// </summary>
        public InputList<Inputs.ResponsePlanTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ResponsePlanTagArgs>());
            set => _tags = value;
        }

        public ResponsePlanArgs()
        {
        }
    }
}
