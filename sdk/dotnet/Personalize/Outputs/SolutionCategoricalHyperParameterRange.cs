// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Personalize.Outputs
{

    /// <summary>
    /// Provides the name and values of a Categorical hyperparameter.
    /// </summary>
    [OutputType]
    public sealed class SolutionCategoricalHyperParameterRange
    {
        /// <summary>
        /// The name of the hyperparameter.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// A list of the categories for the hyperparameter.
        /// </summary>
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private SolutionCategoricalHyperParameterRange(
            string? name,

            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }
}
