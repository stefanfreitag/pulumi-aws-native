// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Fis.Outputs
{

    /// <summary>
    /// Specifies an action for the experiment template.
    /// </summary>
    [OutputType]
    public sealed class ExperimentTemplateAction
    {
        public readonly string ActionId;
        public readonly string? Description;
        /// <summary>
        /// The parameters for the action, if applicable.
        /// </summary>
        public readonly ImmutableDictionary<string, string>? Parameters;
        public readonly ImmutableArray<string> StartAfter;
        /// <summary>
        /// One or more targets for the action.
        /// </summary>
        public readonly ImmutableDictionary<string, string>? Targets;

        [OutputConstructor]
        private ExperimentTemplateAction(
            string actionId,

            string? description,

            ImmutableDictionary<string, string>? parameters,

            ImmutableArray<string> startAfter,

            ImmutableDictionary<string, string>? targets)
        {
            ActionId = actionId;
            Description = description;
            Parameters = parameters;
            StartAfter = startAfter;
            Targets = targets;
        }
    }
}
