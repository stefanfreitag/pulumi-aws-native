// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The ``AWS::ApiGateway::UsagePlan`` resource creates a usage plan for deployed APIs. A usage plan sets a target for the throttling and quota limits on individual client API keys. For more information, see [Creating and Using API Usage Plans in Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html) in the *API Gateway Developer Guide*.
 *  In some cases clients can exceed the targets that you set. Don’t rely on usage plans to control costs. Consider using [](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) to monitor costs and [](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) to manage API requests.
 */
export class UsagePlan extends pulumi.CustomResource {
    /**
     * Get an existing UsagePlan resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): UsagePlan {
        return new UsagePlan(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:apigateway:UsagePlan';

    /**
     * Returns true if the given object is an instance of UsagePlan.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is UsagePlan {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === UsagePlan.__pulumiType;
    }

    /**
     * The associated API stages of a usage plan.
     */
    public readonly apiStages!: pulumi.Output<outputs.apigateway.UsagePlanApiStage[] | undefined>;
    /**
     * The description of a usage plan.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The target maximum number of permitted requests per a given unit time interval.
     */
    public readonly quota!: pulumi.Output<outputs.apigateway.UsagePlanQuotaSettings | undefined>;
    /**
     * The collection of tags. Each tag element is associated with a given resource.
     */
    public readonly tags!: pulumi.Output<outputs.apigateway.UsagePlanTag[] | undefined>;
    /**
     * A map containing method level throttling information for API stage in a usage plan.
     */
    public readonly throttle!: pulumi.Output<outputs.apigateway.UsagePlanThrottleSettings | undefined>;
    /**
     * The name of a usage plan.
     */
    public readonly usagePlanName!: pulumi.Output<string | undefined>;

    /**
     * Create a UsagePlan resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: UsagePlanArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["apiStages"] = args ? args.apiStages : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["quota"] = args ? args.quota : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["throttle"] = args ? args.throttle : undefined;
            resourceInputs["usagePlanName"] = args ? args.usagePlanName : undefined;
        } else {
            resourceInputs["apiStages"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["quota"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["throttle"] = undefined /*out*/;
            resourceInputs["usagePlanName"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(UsagePlan.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a UsagePlan resource.
 */
export interface UsagePlanArgs {
    /**
     * The associated API stages of a usage plan.
     */
    apiStages?: pulumi.Input<pulumi.Input<inputs.apigateway.UsagePlanApiStageArgs>[]>;
    /**
     * The description of a usage plan.
     */
    description?: pulumi.Input<string>;
    /**
     * The target maximum number of permitted requests per a given unit time interval.
     */
    quota?: pulumi.Input<inputs.apigateway.UsagePlanQuotaSettingsArgs>;
    /**
     * The collection of tags. Each tag element is associated with a given resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.apigateway.UsagePlanTagArgs>[]>;
    /**
     * A map containing method level throttling information for API stage in a usage plan.
     */
    throttle?: pulumi.Input<inputs.apigateway.UsagePlanThrottleSettingsArgs>;
    /**
     * The name of a usage plan.
     */
    usagePlanName?: pulumi.Input<string>;
}
