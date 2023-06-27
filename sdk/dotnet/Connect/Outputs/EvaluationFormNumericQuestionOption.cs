// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect.Outputs
{

    /// <summary>
    /// The option ranges used for scoring in numeric questions.
    /// </summary>
    [OutputType]
    public sealed class EvaluationFormNumericQuestionOption
    {
        /// <summary>
        /// The flag to mark the option as automatic fail.
        /// </summary>
        public readonly bool? AutomaticFail;
        /// <summary>
        /// The maximum value of the option range.
        /// </summary>
        public readonly int MaxValue;
        /// <summary>
        /// The minimum value of the option range.
        /// </summary>
        public readonly int MinValue;
        /// <summary>
        /// The score of the option range.
        /// </summary>
        public readonly int? Score;

        [OutputConstructor]
        private EvaluationFormNumericQuestionOption(
            bool? automaticFail,

            int maxValue,

            int minValue,

            int? score)
        {
            AutomaticFail = automaticFail;
            MaxValue = maxValue;
            MinValue = minValue;
            Score = score;
        }
    }
}
