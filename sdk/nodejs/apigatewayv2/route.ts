// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The ``AWS::ApiGatewayV2::Route`` resource creates a route for an API.
 */
export class Route extends pulumi.CustomResource {
    /**
     * Get an existing Route resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Route {
        return new Route(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:apigatewayv2:Route';

    /**
     * Returns true if the given object is an instance of Route.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Route {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Route.__pulumiType;
    }

    /**
     * The API identifier.
     */
    public readonly apiId!: pulumi.Output<string>;
    /**
     * Specifies whether an API key is required for the route. Supported only for WebSocket APIs.
     */
    public readonly apiKeyRequired!: pulumi.Output<boolean | undefined>;
    /**
     * The authorization scopes supported by this route.
     */
    public readonly authorizationScopes!: pulumi.Output<string[] | undefined>;
    /**
     * The authorization type for the route. For WebSocket APIs, valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer. For HTTP APIs, valid values are ``NONE`` for open access, ``JWT`` for using JSON Web Tokens, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer.
     */
    public readonly authorizationType!: pulumi.Output<string | undefined>;
    /**
     * The identifier of the ``Authorizer`` resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.
     */
    public readonly authorizerId!: pulumi.Output<string | undefined>;
    /**
     * The model selection expression for the route. Supported only for WebSocket APIs.
     */
    public readonly modelSelectionExpression!: pulumi.Output<string | undefined>;
    /**
     * The operation name for the route.
     */
    public readonly operationName!: pulumi.Output<string | undefined>;
    /**
     * The request models for the route. Supported only for WebSocket APIs.
     */
    public readonly requestModels!: pulumi.Output<any | undefined>;
    /**
     * The request parameters for the route. Supported only for WebSocket APIs.
     */
    public readonly requestParameters!: pulumi.Output<any | undefined>;
    public /*out*/ readonly routeId!: pulumi.Output<string>;
    /**
     * The route key for the route. For HTTP APIs, the route key can be either ``$default``, or a combination of an HTTP method and resource path, for example, ``GET /pets``.
     */
    public readonly routeKey!: pulumi.Output<string>;
    /**
     * The route response selection expression for the route. Supported only for WebSocket APIs.
     */
    public readonly routeResponseSelectionExpression!: pulumi.Output<string | undefined>;
    /**
     * The target for the route.
     */
    public readonly target!: pulumi.Output<string | undefined>;

    /**
     * Create a Route resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RouteArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.apiId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'apiId'");
            }
            if ((!args || args.routeKey === undefined) && !opts.urn) {
                throw new Error("Missing required property 'routeKey'");
            }
            resourceInputs["apiId"] = args ? args.apiId : undefined;
            resourceInputs["apiKeyRequired"] = args ? args.apiKeyRequired : undefined;
            resourceInputs["authorizationScopes"] = args ? args.authorizationScopes : undefined;
            resourceInputs["authorizationType"] = args ? args.authorizationType : undefined;
            resourceInputs["authorizerId"] = args ? args.authorizerId : undefined;
            resourceInputs["modelSelectionExpression"] = args ? args.modelSelectionExpression : undefined;
            resourceInputs["operationName"] = args ? args.operationName : undefined;
            resourceInputs["requestModels"] = args ? args.requestModels : undefined;
            resourceInputs["requestParameters"] = args ? args.requestParameters : undefined;
            resourceInputs["routeKey"] = args ? args.routeKey : undefined;
            resourceInputs["routeResponseSelectionExpression"] = args ? args.routeResponseSelectionExpression : undefined;
            resourceInputs["target"] = args ? args.target : undefined;
            resourceInputs["routeId"] = undefined /*out*/;
        } else {
            resourceInputs["apiId"] = undefined /*out*/;
            resourceInputs["apiKeyRequired"] = undefined /*out*/;
            resourceInputs["authorizationScopes"] = undefined /*out*/;
            resourceInputs["authorizationType"] = undefined /*out*/;
            resourceInputs["authorizerId"] = undefined /*out*/;
            resourceInputs["modelSelectionExpression"] = undefined /*out*/;
            resourceInputs["operationName"] = undefined /*out*/;
            resourceInputs["requestModels"] = undefined /*out*/;
            resourceInputs["requestParameters"] = undefined /*out*/;
            resourceInputs["routeId"] = undefined /*out*/;
            resourceInputs["routeKey"] = undefined /*out*/;
            resourceInputs["routeResponseSelectionExpression"] = undefined /*out*/;
            resourceInputs["target"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["apiId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Route.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Route resource.
 */
export interface RouteArgs {
    /**
     * The API identifier.
     */
    apiId: pulumi.Input<string>;
    /**
     * Specifies whether an API key is required for the route. Supported only for WebSocket APIs.
     */
    apiKeyRequired?: pulumi.Input<boolean>;
    /**
     * The authorization scopes supported by this route.
     */
    authorizationScopes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The authorization type for the route. For WebSocket APIs, valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer. For HTTP APIs, valid values are ``NONE`` for open access, ``JWT`` for using JSON Web Tokens, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer.
     */
    authorizationType?: pulumi.Input<string>;
    /**
     * The identifier of the ``Authorizer`` resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.
     */
    authorizerId?: pulumi.Input<string>;
    /**
     * The model selection expression for the route. Supported only for WebSocket APIs.
     */
    modelSelectionExpression?: pulumi.Input<string>;
    /**
     * The operation name for the route.
     */
    operationName?: pulumi.Input<string>;
    /**
     * The request models for the route. Supported only for WebSocket APIs.
     */
    requestModels?: any;
    /**
     * The request parameters for the route. Supported only for WebSocket APIs.
     */
    requestParameters?: any;
    /**
     * The route key for the route. For HTTP APIs, the route key can be either ``$default``, or a combination of an HTTP method and resource path, for example, ``GET /pets``.
     */
    routeKey: pulumi.Input<string>;
    /**
     * The route response selection expression for the route. Supported only for WebSocket APIs.
     */
    routeResponseSelectionExpression?: pulumi.Input<string>;
    /**
     * The target for the route.
     */
    target?: pulumi.Input<string>;
}
